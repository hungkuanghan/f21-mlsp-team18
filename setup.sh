# Download training / testing data from dropbox
curl -L https://www.dropbox.com/s/8jk8znpkzjlto9t/nsynth-train.zip?dl=0 -o nsynth-training.zip
curl -L https://www.dropbox.com/s/0nw0madnmq6ckac/nsynth-valid.zip?dl=0 -o nsynth-valid.zip
curl -L https://www.dropbox.com/s/pnpbdlhm7lwcpya/nsynth-test.zip\?dl\=0 -o nsynth-test.zip

# Unzip dataset
unzip nsynth-training.zip
unzip nsynth-valid.zip
unzip nsynth-test.zip

# install sprocket
git clone https://github.com/k2kobayashi/sprocket.git

# create necessary paths
SPROCKET_WAV=./sprocket/example/data/wav/
NSYNTH_ADUIO=./nsynth-train/audio
mkdir -p $SPROCKET_WAV/{ACOUSTIC,ELECTRONIC}
cp $NSYNTH_ADUIO/guitar_acoustic_017-*.wav $SPROCKET_WAV/ACOUSTIC
cp $NSYNTH_ADUIO/guitar_electronic_017-*.wav $SPROCKET_WAV/ELECTRONIC

# Clean up
rm -f *.zip

# install necessary package
pip install -r requirements.txt
