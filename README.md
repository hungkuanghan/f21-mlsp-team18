## How to setup
```bash
sh setup.sh
```

## How to run approach 1 - sprocket to generate wav
```
cd sprocket/example
python3 initialize.py -1 ACOUSTIC ELECTRONIC 16000
# Note that you need to edit the lists in "example/list" directory. Make sure train & eval has no overlapping
python3 initialize.py -2 ACOUSTIC ELECTRONIC 16000
python3 initialize.py -3 ACOUSTIC ELECTRONIC 16000
python3 run_sprocket.py -1 -2 -3 -4 -5 ACOUSTIC ELECTRONIC

# The result wav is in sprocket/example/data/pair/ACOUSTIC-ELECTRONIC/test/ACOUSTIC
```

## How to evaluate mfcc distance
```bash
python3 utils/mfcc_eval.py <path_to_wav1> <path_to_wav2>
```

## How to generate spectrogram picture
```bash
python3 utils/spectrogram_display.py <path_to_wav> <path_to_output_img>
```

## Time-domain Timbre Transformation

The aim is to transfer timbre from one musical source to another musical source, but entirely in the time domain.

Frequency domain methods typically struggle with phase reconstruction issues which time-domain approaches seek to avoid.

The most popular dataset for this is the [NSynth dataset by Magenta](https://magenta.tensorflow.org/datasets/nsynth), though a newer dataset such as [Amp-Space](https://dafx2020.mdw.ac.at/proceedings/papers/DAFx20in21_paper_47.pdf) may be used once it is released.
