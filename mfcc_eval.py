import sys
import librosa
import os
import numpy as np
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
import matplotlib.pyplot as plt
from sklearn import linear_model
from tqdm import tqdm
import pandas as pd
from sklearn.decomposition import NMF

def getMFCC(filepath):
    y, sr = librosa.load(filepath)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    return mfcc.reshape(-1)

if __name__ == '__main__':
    pred = sys.argv[1]
    gt = sys.argv[2]
    print(np.linalg.norm(getMFCC(pred) - getMFCC(gt)))
