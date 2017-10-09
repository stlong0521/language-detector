import os
import sys

def main(build):
    build.executables.run([sys.executable, "language_detector/main.py"])

def download_raw_data(build):
    build.packages.install("pyyaml", version="==3.12")
    build.packages.install("youtube-dl", version="==2017.9.24")
    build.executables.run([sys.executable, "language_detector/data_acquisition/download.py"])

def preprocessing(build):
#    os.environ['SPARK_HOME'] = '/usr/local/share/spark/spark-2.0.2'
#    build.packages.install("opencv-python", version="==3.3.0.10")
#    build.packages.install("matplotlib", version="==1.5.0")
#    build.packages.install("python-speech-features", version="==0.6")
#    build.executables.run([
#        "./language_detector/preprocessing/run.sh",
#        "--input-path", os.path.join(os.getcwd(), "data/raw/english"),
#        "--output-path", os.path.join(os.getcwd(), "data/rst/english")])
#    build.executables.run([
#        "./language_detector/preprocessing/run.sh",
#        "--input-path", os.path.join(os.getcwd(), "data/raw/chinese"),
#        "--output-path", os.path.join(os.getcwd(), "data/rst/chinese")])
    build.executables.run([
        sys.executable, "language_detector/preprocessing/label_data.py",
        "--input-path", os.path.join(os.getcwd(), "data/rst"),
        "--output-path", os.path.join(os.getcwd(), "data/labelled")])

def train_model(build):
    build.packages.install("tensorflow", version="==1.3.0")
    build.packages.install("pillow", version="==4.3.0")
    build.executables.run([
        sys.executable, "language_detector/modeling/train.py",
        "--config", "language_detector/modeling/config.yaml"])

def evaluate_model(build):
    build.packages.install("tensorflow", version="==1.3.0")
    build.packages.install("pillow", version="==4.3.0")
    build.executables.run([
        sys.executable, "language_detector/modeling/evaluate.py",
        "--config", "language_detector/modeling/config.yaml",
        "--model", "snapshots/Berlin_2017-10-08T19-10-39/Berlin.tensormodel-100"])
