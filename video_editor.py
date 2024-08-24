from moviepy.editor import VideoFileClip, concatenate_videoclips
from pydub import AudioSegment
from pydub.silence import detect_nonsilent, detect_silence
import os

videos = ["./videos/vod1.mp4","./videos/vod2.mp4","./videos/vod3.mp4"]
video_folder = "./videos"  # Assuming videos are in a folder named "videos" in the same directory

def trim_video(video_path, start_time, end_time):
    video = VideoFileClip(video_path)
    trimmed_video = video.subclip(start_time, end_time)
    return trimmed_video

# Check if the video file exists before trimming

def concatenate_videos(*video_paths):
    video_clips = []
    for path in video_paths:
        video = VideoFileClip(path)
        video_clips.append(video)
    final_video = concatenate_videoclips(video_clips)
    final_video_path = os.path.join(video_folder, "final_video.mp4")
    final_video.write_videofile(final_video_path)



def mark_silent_times(video_path):
    video = VideoFileClip(video_path)
    audio = video.audio

    # Export audio to a temporary file
    temp_audio_path = "temp_audio.wav"
    audio.write_audiofile(temp_audio_path)

    # Load the audio file with pydub
    audio_segment = AudioSegment.from_file(temp_audio_path, format="wav")

    # Detect silent segments
    audio_segments = detect_silence(audio_segment, min_silence_len=1000)

    print(audio_segments)

    silent_times = []
    for segment in audio_segments:
        if segment[1] - segment[0] > 1000:
            silent_times.append(segment)

    # Clean up the temporary audio file
    #os.remove(temp_audio_path)

    return silent_times

print(mark_silent_times(videos[0]))












''' Testing the functions below
if os.path.exists(videos[0]):
    trimmed_video = trim_video(videos[0], 0, 4)
    trimmed_video_path = os.path.join(video_folder, "trimmed_video.mp4")
    trimmed_video.write_videofile(trimmed_video_path)
else:
    print("Video file not found.")

concatenate_videos(videos[0], videos[1], videos[2])  # Concatenating multiple videos
'''



