import librosa
import os
import numpy as np
import soundfile as sf
import sys

if __name__ == '__main__':
    data_dir, centriod_dir, output_dir, source_family, target_family = sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4], sys.argv[5]

    source_mat = []

    for subdir, dirs, files in os.walk(data_dir):
        for index, file in enumerate(files):
            if file.endswith(".wav"):
                print(file)
                path = os.path.join(subdir, file)
                y, sr = librosa.load(path, sr=16000)
                music_spectrogram = librosa.stft(y, n_fft=2048, hop_length=256, center=False, win_length=2048)
                M = abs(music_spectrogram)  # music file matrix representation, rows are different frequencies, cols are time series
                phase = music_spectrogram / (M + 2.2204e-16)
                if source_family in file:
                    source_mat.append([M,file])

    y, sr = librosa.load(centriod_dir+'/centriod_'+ target_family +'.wav', sr=16000)
    tar_spectrogram = librosa.stft(y, n_fft=2048, hop_length=256, center=False, win_length=2048)
    M_tar = abs(tar_spectrogram)

    y, sr = librosa.load(centriod_dir+'/centriod_'+ source_family +'.wav', sr=16000)
    src_spectrogram = librosa.stft(y, n_fft=2048, hop_length=256, center=False, win_length=2048)
    M_src = abs(src_spectrogram)

    W = np.linalg.pinv(M_src) @ M_tar

    for source, source_filename in source_mat:
        transformed = source @ W
        transformed = librosa.istft(transformed*phase, hop_length=256, center=False, win_length=2048)
        sf.write(output_dir + '/transformed_' + source_filename, transformed, sr)
