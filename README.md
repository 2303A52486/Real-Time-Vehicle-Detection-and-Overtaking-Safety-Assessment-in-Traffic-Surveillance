### Overview:



This project uses an end-to-end vehicle detection pipeline in video from RetinaNet (ResNet-50 FPN backbone).



It detects vehicles in real-time from road cameras and computes other analytics:

* Distance from each vehicle
* Overtaking angle in terms of the camera
* Angle accuracy estimation



The system generates an annotated video with visual overlays and tracks progress batch by batch of processed frames.



### Workflow Summary



1. ##### **Model Used:**



* Model: RetinaNet (torchvision implementation)
* Backbone: ResNet-50 FPN
* Pretrained On: COCO dataset



##### **2. Dataset and Input:**



* Input is a road video that simulates dashcam footage.
* Example input video: sample\_video.mp4
* The vehicle classes alone are identified:

| Class      | COCO ID |
| ---------- | ------- |
| Car        | 3       |
| Motorcycle | 4       |
| Bus        | 6       |
| Truck      | 8       |



##### **3. Video Processing Pipeline:**



* They are batched 8 at a time for quicker inference.
* Each frame undergoes resizing before being processed by RetinaNet.
* Output: bounding boxes, labels, scores.



##### **4. Calculations of Distance and Angle:**



For each automobile discovered:

* **Distance Assessment:**

    **Applies bounding box width and camera calibration formula.**

* **Overtaking Angle:**

  **Calculated by subtracting object center from frame center.**

* **Angle Accuracy:**

  **An accuracy metric founded on angular deviation.**

  

  ##### **5. Visualization:**

  

* Bounding boxes in Yellow (default).
* Labels show:

   	\[Class], D: \[Distance in meters], A: \[Angle in degrees] | Acc: \[Accuracy in %]

  

  **Example:**

   	car, D: 15.2m, A: 5.3° | Acc: 94.7%

  

  ##### **6. Execution Command:**

  

* Run in Colab or locally:

   	python retinanet\_pipeline.py --input sample\_video.mp4 --output output\_video.mp4

  

  ##### **7. Final Outputs:**

  

* Processed Video: output\_video.mp4
* Log Outputs: Frame progress logs every 50 frames
* Visual Overlays: Boxes, distances, angles, in output video

  

  ### Evaluation Summary:
| Metric                | Description                    |
| --------------------- | ------------------------------ |
| Batch Size            | 8 frames                       |
| Inference Speed       | Moderate (GPU recommended)     |
| Detection Classes     | Vehicle-only                   |
| Visualization         | Bounding boxes + Text overlays |

  

  

  ###### Conclusion:

  This project provides an actual application of RetinaNet-based car detection with additional driving analytics such as overtaking angle estimation and distance calculation. The pipeline is modular, extensible, and it can be adapted to traffic analysis as well as real-time driver assistance systems.

  

  ### LICENSE:

  
All Rights Reserved © 2025 Vajinapalli Abhinav.

  
This project is shared publicly *only for resume, portfolio, and internship/job application purposes*.

  

* **Reproduction, reuse, or distribution is strictly prohibited.**

  

