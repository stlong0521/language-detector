# Language Detector
Detect which language it is from speech. More details to follow.

# Requirements
* Python2.7
* FFmpeg (convert audios to wav format): [How to install](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
* Freetype and png (preprocessing needed): ```sudo apt-get install libfreetype6-dev; sudo apt-get install libpng-dev```
* Spark (preprocessing, convert wav audios to spectrogram images): [How to install](http://blog.prabeeshk.com/blog/2016/12/07/install-apache-spark-2-on-ubuntu-16-dot-04-and-mac-os/)
* Tensorflow (train neural network models): managed by uranium, no need to install manually

# Acknowledgment
This project is inspired by and a large portion of codes comes from the great work [here](https://github.com/twerkmeister/iLID).
