import sys

def main(build):
    build.executables.run([sys.executable, "language_detector/main.py"])

def download_raw_data(build):
    # If complained by audio format errors, uncomment the 4 lines below to install ffmpeg
    # Ubuntu only, find the proper way to install ffmpge for other OS
    # build.executables.run(["sudo", "add-apt-repository", "ppa:mc3man/trusty-media"])
    # build.executables.run(["sudo", "apt-get", "update"])
    # build.executables.run(["sudo", "apt-get", "install", "ffmpeg"])
    # build.executables.run(["sudo", "apt-get", "install", "frei0r-plugins"])
    build.packages.install("pyyaml", version="==3.12")
    build.packages.install("youtube-dl", version="==2017.9.24")
    build.executables.run([sys.executable, "language_detector/data_acquisition/download.py"])
