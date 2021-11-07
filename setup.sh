# Download training / testing data from dropbox
curl -L https://www.dropbox.com/s/8jk8znpkzjlto9t/nsynth-train.zip?dl=0 -o nsynth-training.zip
curl -L https://www.dropbox.com/s/0nw0madnmq6ckac/nsynth-valid.zip?dl=0 -o nsynth-valid.zip
curl -L https://www.dropbox.com/s/pnpbdlhm7lwcpya/nsynth-test.zip\?dl\=0 -o nsynth-test.zip

# Unzip dataset
unzip nsynth-training.zip
unzip nsynth-valid.zip
unzip nsynth-test.zip

# install necessary package
pip install -r requirements.txt
