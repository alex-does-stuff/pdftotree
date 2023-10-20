echo "Downloading pretrained vision model..."
url=http://i.stanford.edu/hazy/share/fonduer/visualtable/paleo_visual_model.h5
data_file=paleo_visual_model.h5
curl -RLO $url
echo "Done!"
