import librosa
import os
import soundfile as sf


data_dir = '../data/nsynth-train/audio'
output_dir = '../'

shifted_data_mat = []

for subdir, dirs, files in os.walk(data_dir):
    for index, file in enumerate(files):
        if file.endswith(".wav"):
            print(file + '    ' + str(index) + '/' +str(len(files)))
            path = os.path.join(subdir, file)
            labels = os.path.splitext(file)[0].split('-')
            amp = labels[-1]
            pitch = labels[-2]
            pitch = int(pitch.lstrip('0'))
            steps = 69 - pitch
            y, sr = librosa.load(path, sr=16000)
            y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=steps)
            sf.write('../processed_data/'+'pitch_shifted_'+file, y_shifted, sr)
            shifted_data_mat.append(y_shifted)

