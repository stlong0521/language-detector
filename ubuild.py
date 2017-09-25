import os
import sys

def main(build):
    build.executables.run([sys.executable, "language_detector/main.py"])

def download_raw_data(build):
    build.packages.install("pyyaml", version="==3.12")
    build.packages.install("youtube-dl", version="==2017.9.24")
    build.executables.run([sys.executable, "language_detector/data_acquisition/download.py"])

def preprocessing(build):
    os.environ['SPARK_HOME'] = '/usr/local/share/spark/spark-2.0.2'
    build.executables.run(["./language_detector/preprocessing/run_preprocessing_spark_job.sh"])
