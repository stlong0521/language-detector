import sys

def main(build):
    build.executables.run([sys.executable, "language_detector/main.py"])
