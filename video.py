from ultralytics import YOLO
import cv2
import argparse

def process_video(video_path, model_path, output_path):
    FULL_VIDEO = True
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("fps",fps)
    out = cv2.VideoWriter(output_path, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

    # Get total frame count for progress bar
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_sec = 10
    num_frames = int(fps * duration_sec)
    # Initialize progress bar
    frame_count = 0
    while cap.isOpened() and (frame_count < num_frames or FULL_VIDEO) :
        if frame_count%fps <=1:
            print(int(frame_count/fps),"sec / total:",int(total_frames/fps), "sec")
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, verbose=False)
        out.write(results[0].plot())
        frame_count += 1

    cap.release()
    out.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a video with YOLO object detection.")
    parser.add_argument('video_path', type=str, help="Path to the input video file")
    parser.add_argument('model_path', type=str, help="Path to the YOLO model file")
    parser.add_argument('output_path', type=str, help="Path to the output video file")

    args = parser.parse_args()
    process_video(args.video_path, args.model_path, args.output_path)
    # process_video("my_video.mp4","my_model.pt","my_predicted_video.mp4")
    # python your_script.py input_video.mp4 your_model.pt output_video.mp4

