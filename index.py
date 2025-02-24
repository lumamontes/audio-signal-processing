from flask import Flask, render_template, send_from_directory
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)

# Path to the audio folder
audio_folder = '/app/audio_files/'
static_folder = '/app/static/images/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio')
def process_audio():
    audio_file = 'overflow.mp3' 

    audio_path = os.path.join(audio_folder, audio_file)
    y, sr = librosa.load(audio_path)

    plt.style.use('seaborn-v0_8-whitegrid')
    # Create waveform plot
    plt.figure(figsize=(12, 6))
    librosa.display.waveshow(y, sr=sr, color='cyan')
    plt.title('Waveform of Audio', fontsize=16)
    plt.xlabel('Time (s)', fontsize=14)
    plt.ylabel('Amplitude', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.savefig('/app/static/images/waveform.png', dpi=300)
    plt.close()


    # Uses the Fast Fourier Transform
    fft_result = np.fft.fft(y)
    frequencies = np.fft.fftfreq(len(fft_result), 1/sr)

    # Create frequency spectrum plot
    plt.figure(figsize=(12, 6))
    plt.plot(frequencies[:len(frequencies)//2], np.abs(fft_result)[:len(fft_result)//2], color='magenta', linewidth=2)
    plt.title('Frequency Spectrum of Audio', fontsize=16)
    plt.xlabel('Frequency (Hz)', fontsize=14)
    plt.ylabel('Amplitude', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.savefig('/app/static/images/frequency_spectrum.png', dpi=300)
    plt.close()


    return render_template('results.html', waveform='images/waveform.png', spectrum='images/frequency_spectrum.png')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

@app.route('/static/overflow.mp3')
def serve_audio():
    return send_from_directory(audio_folder, 'overflow.mp3')
