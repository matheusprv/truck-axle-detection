# Dataset

Truck axle detection and counting dataset. 

For detection task, the dataset is made over the [YOLOv11](https://docs.ultralytics.com/datasets/detect/#ultralytics-yolo-format) format, where the bounding boxes were created with [Roboflow](https://app.roboflow.com/truck-axle). The data has already gone through data augmentation from the exporting Roboflow process. 

For counting task, on each subfolder there sis a .txt file with the referenced image file and the number of axles that it contains.

The original dataset can be found [here](https://zenodo.org/records/5744737), but lacks annotation.

# Data Distribution
The original dataset contains 725 images. From these, 80% was used for training, 15% for validation and 15% for test.

The training images went through an augmentation process which resulted in 1521 training images.

Final data distribution can be found in the table below

| Train | Validation | Test |  
|:-----:|:----------:|:----:|
| 1521  | 109        | 109  |  
