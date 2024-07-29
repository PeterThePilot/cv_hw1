# Object Detection Repository

## Overview

Readme file for the HW1 in computer vision in surgiacl application
## Project Structure

- `requirements.txt` - Lists the dependencies needed to run the code.
- `environment.yml` - Lists the dependencies needed to run the code and for easy conda env creation.
- `predict.py` - Script to run predictions on a single image.
- `video.py` - Script to run predictions on a video using OpenCV.

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/PeterThePilot/cv_hw1.git
   cd cv_hw1
   
 2. **Create and Activate a Virtual Environment:**

    ```bash
    conda env create -f environment.yml
    conda activate cv_hw1_env
    ```
    

## Running Predictions
### Image Prediction
To run predictions on an image, use the predict.py script. You need to provide the path to the image as a command-line argument.

    python predict.py input_image.png your_model.pt output_image.png

# Video Prediction
    python video.py input_video.mp4 your_model.pt output_video.mp4


# Model Weights
The final model weights are required for running predictions. You can download the weights from the following link:

Download Model Weights

Please ensure you place the downloaded weights in the appropriate directory as specified in the scripts.

# Video Demonstration
A demonstration video showing bounding boxes on an out-of-distribution (OOD) video is available at:

Watch Video


