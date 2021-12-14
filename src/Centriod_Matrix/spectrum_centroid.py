import librosa
import os
import numpy as np
import soundfile as sf
import sys

if __name__ == '__main__':

    data_dir, output_dir, source_family, target_family, pitch_center, pitch_range = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), int(sys.argv[6])

    target_mat = np.zeros((1025, 243))
    source_mat = np.zeros((1025, 243))
    count_tar = 0
    count_src = 0

    for subdir, dirs, files in os.walk(data_dir):
        for index, file in enumerate(files):
            if file.endswith(".wav"):
                labels = os.path.splitext(file)[0].split('-')
                pitch = labels[-2]
                pitch = int(pitch.lstrip('0'))
                if abs(pitch_center-pitch) <= pitch_range:
                    print(file)
                    path = os.path.join(subdir, file)
                    y, sr = librosa.load(path, sr=16000)
                    music_spectrogram = librosa.stft(y, n_fft=2048, hop_length=256, center=False, win_length=2048)
                    M = abs(music_spectrogram)
                    phase = music_spectrogram / (M + 2.2204e-16)
                    if target_family in file:
                        target_mat = target_mat + M
                        count_tar += 1
                    elif source_family in file:
                        source_mat = source_mat + M
                        count_src += 1

    source_mat = source_mat / count_src
    target_mat = target_mat / count_tar

    acc_avg = librosa.istft(source_mat * phase, hop_length=256, center=False, win_length=2048)
    sf.write(output_dir + '/centriod_'+source_family+'.wav', acc_avg, sr)

    ele_avg = librosa.istft(target_mat * phase, hop_length=256, center=False, win_length=2048)
    sf.write(output_dir + '/centriod_'+target_family + '.wav', ele_avg, sr)

