import os
import scipy.io.wavfile as wav
from eggs.utils import filename_cleaner

def read_wav(f):
    samplerate, signal = wav.read(f)
    f = filename_cleaner.truncate_extension(filename_cleaner.clean(f))
    return f, samplerate, signal

def save_wav(f, samplerate, signal, output_path):
    f = os.path.join(output_path, os.path.basename(f) + '.wav')
    wav.write(f, samplerate, signal)
