import sys
import librosa
import numpy as np

def getMFCC(filepath):
    y, sr = librosa.load(filepath)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    return mfcc.reshape(-1)

if __name__ == '__main__':
    pred = sys.argv[1]
    gt = sys.argv[2]
    print(np.linalg.norm(getMFCC(pred) - getMFCC(gt)))
