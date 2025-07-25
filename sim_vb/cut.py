# Cut all the .wav in this folder to length 3*48000

import os
import numpy as np
import soundfile as sf
import librosa

def cut_audio_to_length(audio_path, target_length=3*48000):
    """Cut audio to a specific length."""
    audio, sr = librosa.load(audio_path, sr=None)
    if len(audio) > target_length:
        audio = audio[:target_length]
    elif len(audio) < target_length:
        audio = np.pad(audio, (0, max(0, target_length - len(audio))), mode='constant')
    return audio, sr

for file in os.listdir():
    if file.endswith('.wav'):
        audio_path = file
        cut_audio, sr = cut_audio_to_length(audio_path)
        sf.write(audio_path, cut_audio, sr)