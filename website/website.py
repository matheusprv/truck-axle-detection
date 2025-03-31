from flask import Flask, request, render_template, jsonify
from PIL import Image
import io
import cv2
import numpy as np
import base64
from ultralytics import YOLO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    image = Image.open(file.stream)
    image = np.array(image)

    processed_image, num_boxes = make_inference(image)

    img_io = io.BytesIO()
    pil_image = Image.fromarray(processed_image)
    pil_image.save(img_io, format='PNG')
    img_io.seek(0)
    base64_img = base64.b64encode(img_io.getvalue()).decode('utf-8')

    return jsonify({
        'image': base64_img,
        'total_boxes': num_boxes
    })

def make_inference(image):
    print("Carregando o modelo")
    model_path = "./models/yolov12.pt"
    model = YOLO(model_path)
    print("Modelo carregado")

    original_height, original_width, _ = image.shape

    print("Fazendo inferencia")
    img_resized = cv2.resize(image, (640, 640))
    results = model.predict(img_resized, save=False)

    print("Processando imagem final")
    for box in results[0].boxes:
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        class_item = results[0].names[box.cls[0].item()]
        confidence = round(box.conf[0].item(), 2)

        # Scale coordinates back to original image size
        x1, y1, x2, y2 = cords
        x1 = int(x1 * (original_width / 640))
        y1 = int(y1 * (original_height / 640))
        x2 = int(x2 * (original_width / 640))
        y2 = int(y2 * (original_height / 640))

        # Draw bounding box on the image
        color = (255, 0, 0)
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 3)

        # Adding the class and confidence on each prediction
        text = f"{class_item} {confidence:.2f}"
        (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
        cv2.rectangle(image, (x1, y1 - th - 5), (x1 + tw + 5, y1), color, -1)
        cv2.putText(image, text, (x1 + 2, y1 - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    print("retornando imagem")
    return image, len(results[0].boxes)

if __name__ == '__main__':
    app.run(debug=True)
