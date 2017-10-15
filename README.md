# Language Detector
Detect which language it is from speech (Chinese or English).

# Requirements
* Python2.7
* FFmpeg (convert audios to wav format): [How to install](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
* Freetype and png (preprocessing needed): `sudo apt-get install libfreetype6-dev; sudo apt-get install libpng-dev`
* Spark (preprocessing, convert wav audios to spectrogram images): [How to install](http://blog.prabeeshk.com/blog/2016/12/07/install-apache-spark-2-on-ubuntu-16-dot-04-and-mac-os/)
* Tensorflow (train neural network models): managed by uranium, no need to install manually

# Data & Results
* Raw data: 635 minutes of Chinese interviews from Luyu Official (i.e., Lu Yu You Yue), and 534 minutes of English interviews from Ellen Show, both on Youtube
* Processed data: 38122 spectrogram images for Chinese interviews, and 32079 spectrogram images for English interviews (one image for one second of speech)
* Train/test data split: processed data are mixed, shuffled and split into train/test sets by 80%/20%
* Evaluation accuracy: 92.7% (on test set) achieved from Berlinnet neural network model trained by 19300 iterations

# How to Use
1. Download raw data from Youtube; the downloaded data will be under `./data/raw/`

   ```./uranium download```
   > You can customize your download list in `./language_detection/data_acquisition/sources.yml`

2. Preprocess (using Spark) raw data and label; the processed data (spectrogram images) will be under `./data/rst/`, and labelled spectrogram image indices will be under `./data/labelled/`

   ```./uranium preprocess```

3. Train (using Tensorflow) the neural network model; the trained model  will be under `./snapshots/`

   ```./uranium train```
   > The neural network model, `Berlinnet` (a shallow network model adopted from [here](https://github.com/twerkmeister/iLID/blob/master/tensorflow/network/instances/berlinnet.py)), is used by default; tweak the configuration in `./language_detector/modeling/config.yaml' if necessary

   > Depending on the desired number of training iterations and your hardware, it could take hours to days

   > To visualize the model and training progress via TensorBoard, run `./uranium visualize` and go to `localhost:6006`

4. Evaluate the trained model on the test data set

   ```./uranium evaluate```
   > You can do this no matter whether the training is complete or not; when the training is still in progress, the evaluation is performed upon the checkpoint wherever the training progress is

   > Set up the checkpoint properly by making modification [here](https://github.com/stlong0521/language-detector/blob/master/ubuild.py#L39)

# Acknowledgment
This project is inspired by and a large portion of codes comes from the great work [here](https://github.com/twerkmeister/iLID).
