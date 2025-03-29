# Truck Axle Detection

Project developed under the discipline BCC406 - Neural Network and Deep Learning from the Federal University of Ouro Preto.

In many Brazilian cities, trucks with more axles than a certain threshold are prohibited from circulating. However, enforcement of this rule is often lacking. In light of this issue, the objective of this project is to investigate the use of neural networks to automatically identify the number of axles on a truck from an image.

Detailed information about the dataset used can be found in the [Dataset directory](./Dataset/).

Two main approaches were explored in this project:

* **Object Detection**: Identifying the position of the axles using YOLO.
* **Regression Models**: Predicting the number of axles directly from the image

All trained models are available in the [Model directory](./Model/).

## Detection models
Using YOLOv11m and YOLOv12m to detect the axles resulted in excellent results, as can be seen in the following table. 

| Modelo    | mAP50 | mAP75 | mAP50-95 | Precisão | Revocação | F1 Score |
|:---------:|:-----:|:-----:|:---------:|:---------:|:----------:|:--------:|
| YOLOv11m  | 0.99  | 0.93  | 0.77      | 0.99      | 0.99       | 0.99     |
| YOLOv12m  | 0.99  | 0.94  | 0.77      | 0.99      | 0.99       | 0.99     |

An example of YOLOv11m's predictions can be seen in the image below:

![Imagem](Relatorio/Images/yolo_outputs/yolo_output_20170418095402_color-[ROI-1]-94(1).jpg)

## Counting models
The second approach uses regression models to estimate the number of axles. These models receive an image as input and output a real number, which is then rounded to the nearest integer to produce the final prediction.

The architecture of the models is shown below. In the "Transfer Learning" section, InceptionV3 and ResNet152 were used as base models.

![Models](Relatorio/Images/modelo.png)

To allow comparison between detection and regression approaches, the number of bounding boxes detected by the YOLO models was used as an estimate of the axle count. The results of this comparison are shown in the table below:


| Modelo       | Precision | Recall | F1 Score | Acurácia | Teste loss | MAE Loss |
|:------------:|:---------:|:------:|:--------:|:--------:|:-----------:|:---------:|
| ResNet152    | 0.85      | 0.87   | 0.85     | 0.91     | 0.10        | 0.24      |
| InceptionV3  | 0.88      | 0.85   | 0.86     | 0.92     | 0.12        | 0.22      |
| **YOLOv11m** | **0.93**  |**0.95**|**0.94**  | **0.96** | **0.06**    | **0.05**  |
| YOLOv12m     | 0.91      | 0.92   | 0.92     | 0.94     | 0.08        | 0.06      |

