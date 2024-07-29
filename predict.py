from ultralytics import YOLO
import cv2
import argparse

def predict_image(image_path, model_path, predicted_image_path):
    model = YOLO(model_path) #12
    results = model(image_path)
    results[0].save(predicted_image_path)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict objects in an image using a YOLO model.")
    parser.add_argument('image_path', type=str, help="Path to the input image file")
    parser.add_argument('model_path', type=str, help="Path to the YOLO model file")
    parser.add_argument('predicted_image_path', type=str, help="Path to save the predicted image")

    args = parser.parse_args()
    predict_image(args.image_path, args.model_path, args.predicted_image_path)
    # predict_image("my_image.png","my_model.pt","my_predicted_image.png")
    # python your_script.py input_image.png your_model.pt output_image.png
