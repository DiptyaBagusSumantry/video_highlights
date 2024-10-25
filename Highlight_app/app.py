from flask import Flask, request, send_from_directory, jsonify, abort
from moviepy.editor import VideoFileClip
from flask_cors import CORS
import numpy as np
import soundfile as sf
from scipy.signal import find_peaks
import os
import uuid

app = Flask(__name__)
CORS(app, resources={r"/get-video/*": {"origins": ["http://localhost:5173", "http://34.72.25.183:5170", "http://localhost:5170", "http://127.0.0.1:5170"], "methods": ["GET", "POST", "OPTIONS"]}})


def extract_audio_from_video(video_file):
    try:
        video = VideoFileClip(video_file)
        audio_file = video_file.replace(".mp4", ".wav")
        video.audio.write_audiofile(audio_file)
        return audio_file
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None

def detect_audio_spikes_in_chunks(audio_file, threshold=0.9, chunk_size=1024):
    peaks_total = []
    print("Start detecting audio spikes...")
    try:
        with sf.SoundFile(audio_file) as f:
            sample_rate = f.samplerate
            while True:
                chunk = f.read(chunk_size)
                if not chunk.size:
                    break
                if len(chunk.shape) > 1:
                    chunk = np.mean(chunk, axis=1)
                amplitude = np.abs(chunk)
                peaks, _ = find_peaks(amplitude, height=threshold)
                peaks_total.extend(peaks + f.tell() - len(chunk))
        print(f"Audio spike detection completed. {len(peaks_total)} spikes detected.")
        return peaks_total, sample_rate
    except Exception as e:
        print(f"Error detecting spikes: {e}")
        return [], None

def trim_video(video_file, start_time, duration, output_folder):
    try:
        video = VideoFileClip(video_file)
        end_time = min(video.duration, start_time + duration)
        trimmed_clip = video.subclip(start_time, end_time)
        os.makedirs(output_folder, exist_ok=True)
        chunk_filename = f"{output_folder}/{uuid.uuid4()}.mp4"
        trimmed_clip.write_videofile(chunk_filename, codec="libx264")
        print(f"Video successfully trimmed and saved to: {chunk_filename}")
        return chunk_filename
    except Exception as e:
        print(f"Error trimming video: {e}")
        return None

@app.route('/process-video', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video file provided."}), 400

    video_file = request.files['video']
    timestamp = request.form['timestamp']
    
    video_path = f"./{video_file.filename}"
    video_file.save(video_path)
    output_folder = f"./output/{timestamp}"

    audio_file = extract_audio_from_video(video_path)
    if audio_file:
        audio_peaks, sample_rate = detect_audio_spikes_in_chunks(audio_file)

        if audio_peaks:
            print(f"Detected {len(audio_peaks)} audio spikes.")
            minimum_gap = 20
            last_time = -minimum_gap

            for peak in audio_peaks:
                start_time = max(0, peak / sample_rate - 5)
                if start_time - last_time >= minimum_gap:
                    trim_video(video_path, start_time, 20, output_folder)
                    last_time = start_time
        else:
            return jsonify({"message": "No significant audio spikes detected."}), 200
    else:
        return jsonify({"error": "Audio extraction failed."}), 500

    return jsonify({"message": "Processing completed."}), 200

DOMAIN_NAME = 'http://127.0.0.1:5000'
OUTPUT_DIRECTORY = 'output' 

@app.route('/get-video/<folder_name>', methods=['GET'])
def get_videos(folder_name):
    folder_path = os.path.join(OUTPUT_DIRECTORY, folder_name)

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        abort(404) 

    video_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    video_urls = [f"{DOMAIN_NAME}/output/{folder_name}/{video}" for video in video_files]

    return jsonify(video_urls)

@app.route('/output/<folder_name>/<filename>', methods=['GET'])
def serve_video(folder_name, filename):
    folder_path = os.path.join(OUTPUT_DIRECTORY, folder_name)

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        abort(404) 

    try:
        return send_from_directory(folder_path, filename)
    except FileNotFoundError:
        abort(404) 


if __name__ == '__main__':
    app.run(debug=True)






# from flask import Flask, request, jsonify
# from moviepy.editor import VideoFileClip
# import numpy as np
# import soundfile as sf
# from scipy.signal import find_peaks
# import os
# import uuid

# app = Flask(__name__)

# def extract_audio_from_video(video_file):
#     try:
#         video = VideoFileClip(video_file)
#         audio_file = video_file.replace(".mp4", ".wav")
#         video.audio.write_audiofile(audio_file)
#         return audio_file
#     except Exception as e:
#         print(f"Error extracting audio: {e}")
#         return None

# def detect_audio_spikes_in_chunks(audio_file, threshold=0.9, chunk_size=1024):
#     peaks_total = []
#     print("Start detecting audio spikes...")
#     try:
#         with sf.SoundFile(audio_file) as f:
#             sample_rate = f.samplerate
#             while True:
#                 chunk = f.read(chunk_size)
#                 if not chunk.size:
#                     break
#                 if len(chunk.shape) > 1:
#                     chunk = np.mean(chunk, axis=1)
#                 amplitude = np.abs(chunk)
#                 peaks, _ = find_peaks(amplitude, height=threshold)
#                 peaks_total.extend(peaks + f.tell() - len(chunk))
#         print(f"Audio spike detection completed. {len(peaks_total)} spikes detected.")
#         return peaks_total, sample_rate
#     except Exception as e:
#         print(f"Error detecting spikes: {e}")
#         return [], None

# def trim_video(video_file, start_time, duration, output_folder):
#     try:
#         video = VideoFileClip(video_file)
#         end_time = min(video.duration, start_time + duration)
#         trimmed_clip = video.subclip(start_time, end_time)
#         os.makedirs(output_folder, exist_ok=True)
#         chunk_filename = f"{output_folder}/{uuid.uuid4()}.mp4"
#         trimmed_clip.write_videofile(chunk_filename, codec="libx264")
#         print(f"Video successfully trimmed and saved to: {chunk_filename}")
#         return chunk_filename
#     except Exception as e:
#         print(f"Error trimming video: {e}")
#         return None

# @app.route('/process_video', methods=['POST'])
# def process_video():
#     # Mengambil data dari body permintaan
#     data = request.get_json()
    
#     # Memastikan video_path ada dalam request
#     video_path = data.get('video_path')
#     print(f"Video path received: {video_path}")
#     if not video_path or not os.path.isfile(video_path):
#         return jsonify({"error": "Invalid video path provided."}), 400
    
#     output_folder = './output'
    
#     # Ekstrak audio dari video dan deteksi lonjakan audio
#     audio_file = extract_audio_from_video(video_path)
#     if audio_file:
#         audio_peaks, sample_rate = detect_audio_spikes_in_chunks(audio_file)

#         if audio_peaks:
#             print(f"Detected {len(audio_peaks)} audio spikes.")
#             minimum_gap = 20  # seconds
#             last_time = -minimum_gap

#             # Membuat potongan video berdasarkan lonjakan yang terdeteksi
#             for peak in audio_peaks:
#                 start_time = max(0, peak / sample_rate - 5)  # Konversi lonjakan ke waktu dalam detik
#                 if start_time - last_time >= minimum_gap:
#                     trim_video(video_path, start_time, 20, output_folder)
#                     last_time = start_time
#         else:
#             return jsonify({"message": "No significant audio spikes detected."}), 200
#     else:
#         return jsonify({"error": "Audio extraction failed."}), 500

#     return jsonify({"message": "Processing completed."}), 200

# if __name__ == '__main__':
#     app.run(debug=True)
