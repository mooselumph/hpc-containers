#!/bin/bash
cd ./images

function gdrive_download () {
  CONFIRM=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=$1" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')
  wget -nc --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$CONFIRM&id=$1" -O $2
  rm -rf /tmp/cookies.txt
}

gdrive_download 1brJOmjTW2bXWbw33QRiskXs7cXsuqV6H conda37_mpich.sif
gdrive_download 1BzecTpw9B4WpH6vkzUGstwyJCwSq-EXV conda37_ompi.sif
gdrive_download 15Yi82taMdd9lS-nQ9klyk0vMdvKYrR71 py38_mpich_docker.sif
gdrive_download 1Eop_cQr2l9uXwKb0NroA6T933L40BlNi py38_mpich_obspy_docker.sif
gdrive_download 1uCQdAd11ig-UbpwLcJ9J60arv5aXG9qJ conda37_pytorch.sif

cd ../