# coding=utf-8
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import librosa.display
import sys

import numpy as np
import librosa


if __name__ == '__main__':
    src = sys.argv[1]
    desc = sys.argv[2]

    y, sr = librosa.load(src)
    y = y[:100000] # shorten audio a bit for speed

    window_size = 1024
    window = np.hanning(window_size)
    stft  = librosa.core.spectrum.stft(y, n_fft=window_size, hop_length=512, window=window)
    out = 2 * np.abs(stft) / np.sum(window)

    # For plotting headlessly
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

    fig = plt.Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    p = librosa.display.specshow(librosa.amplitude_to_db(out, ref=np.max), ax=ax, y_axis="log", x_axis="time")
    fig.savefig(desc)
