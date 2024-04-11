import cv2

# Open the video file
input_video_path = 'input_video.mp4'
output_video_path = 'output_video_slowed.mp4'
capture = cv2.VideoCapture(input_video_path)

# Get the video properties
fps = capture.get(cv2.CAP_PROP_FPS)
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create VideoWriter object with reduced frame rate
output_video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps * 0.5, (frame_width, frame_height))

# Read and write each frame of the video
while True:
    ret, frame = capture.read()
    if not ret:
        break
    output_video.write(frame)

# Release resources
capture.release()
output_video.release()

