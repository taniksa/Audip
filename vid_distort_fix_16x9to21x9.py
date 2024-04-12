import cv2
import os
import subprocess

def resize_video(input_path, output_path, target_width, target_height, original_fps):
    # Open the video file
    cap = cv2.VideoCapture(input_path)
    
    # Get the original video frame width and height
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Calculate the aspect ratio of the original video
    original_aspect_ratio = original_width / original_height
    
    # Calculate the aspect ratio of the target size
    target_aspect_ratio = target_width / target_height
    
    # Calculate the new dimensions for resizing
    if original_aspect_ratio > target_aspect_ratio:
        new_width = target_width
        new_height = int(target_width / original_aspect_ratio)
    else:
        new_height = target_height
        new_width = int(target_height * original_aspect_ratio)
    
    # Define the codec for the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    # Create VideoWriter object for output video with original FPS
    out = cv2.VideoWriter(output_path, fourcc, original_fps, (target_width, target_height))
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            # Resize the frame to fit the 21:9 aspect ratio
            resized_frame = cv2.resize(frame, (target_width, target_height))
            
            # Write the resized frame to the output video
            out.write(resized_frame)
            
            # Display the resized frame
            cv2.imshow('Resized Frame', resized_frame)
            
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def process_video(input_video_path, target_width, target_height, ffmpeg_path):
    # Get original video FPS
    cap = cv2.VideoCapture(input_video_path)
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    
    output_video_path = f"resized_{input_video_path}"
    print(f"Processing {input_video_path}...")
    resize_video(input_video_path, output_video_path, target_width, target_height, original_fps)
    
    # Extract audio from the original video
    audio_output_path = f"audio_{input_video_path}.aac"
    subprocess.run([ffmpeg_path, '-i', input_video_path, '-q:a', '0', '-map', 'a', audio_output_path])

    # Combine resized video and original audio with sync
    final_output_path = f"final_resized_{input_video_path}"
    subprocess.run([ffmpeg_path, '-i', output_video_path, '-i', audio_output_path, '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', '-async', '1', final_output_path])

    # Remove temporary audio file
    os.remove(audio_output_path)

# Target width and height for 21:9 aspect ratio
target_width = 2560  # for 21:9 aspect ratio
target_height = 1080

# Full path to ffmpeg executable
ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"

# List all files in the current directory
file_list = [f for f in os.listdir() if os.path.isfile(f)]

# Filter video files
video_files = [f for f in file_list if f.endswith(('.mp4', '.avi', '.mkv', '.mov'))]

# Resize each video file
for input_video_path in video_files:
    process_video(input_video_path, target_width, target_height, ffmpeg_path)

print("All videos have been processed.")
