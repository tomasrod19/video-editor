from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, TextClip

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


#grabs all noisy times in the video, makes list of them

def mark_noisy_times(video_path):
    video = VideoFileClip(video_path)
    audio = video.audio

    # Export audio to a temporary file
    temp_audio_path = "temp_audio.wav"
    audio.write_audiofile(temp_audio_path)

    # Load the audio file with pydub
    audio_segment = AudioSegment.from_file(temp_audio_path, format="wav")

    # Detect non-silent segments
    audio_segments = detect_nonsilent(audio_segment, min_silence_len=1000, silence_thresh=-30)

    # Clean up the temporary audio file
    os.remove(temp_audio_path)

    for sec in range(len(audio_segments)):
        audio_segments[sec][0] -= 300
        audio_segments[sec][1] += 300

    return audio_segments

print(mark_noisy_times(videos[0]))

# Trim the video based on the noisy segments

def trim_video_based_on_noise(video_path):
    noisy_segments = mark_noisy_times(video_path)
    video_clips = []
    video = VideoFileClip(video_path)

    for segment in noisy_segments:
        start_time = segment[0] / 1000  # Convert milliseconds to seconds
        end_time = segment[1] / 1000  # Convert milliseconds to seconds
        trimmed_video = video.subclip(start_time, end_time)
        video_clips.append(trimmed_video)

    final_video = concatenate_videoclips(video_clips)
    final_video_path = os.path.join(video_folder, "trimmed_video.mp4")
    final_video.write_videofile(final_video_path)

# Example usage

trim_video_based_on_noise(videos[0])


#next function: subtitles on video