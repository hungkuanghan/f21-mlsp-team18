import librosa
import os
import soundfile as sf
import sys

if __name__ == '__main__':
    data_dir, output_dir, pitch_center, pitch_range = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

    for subdir, dirs, files in os.walk(data_dir):
        for index, file in enumerate(files):
            if file.endswith(".wav"):
                print(file + '  ' + str(index) + '/' +str(len(files)))
                path = os.path.join(subdir, file)
                labels = os.path.splitext(file)[0].split('-')
                amp = labels[-1]
                pitch = labels[-2]
                pitch = int(pitch.lstrip('0'))
                steps = pitch_center - pitch
                if abs(steps) <= pitch_range:
                    y, sr = librosa.load(path, sr=16000)
                    y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=steps)
                    sf.write(output_dir+'/pitch_shifted_'+file, y_shifted, sr)

