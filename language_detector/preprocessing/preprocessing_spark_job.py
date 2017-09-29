from pyspark import SparkContext
from eggs.utils import argparser, file_collector, wav_operator

def main(args):
    files = file_collector.collect(args.input_path)
    sc = SparkContext("local", "preprocessing_spark_job")
    pipeline = (
        sc.parallelize(files, 4)
            .map(lambda f: wav_operator.read_wav(f))
            .map(lambda (f, samplerate, signal): wav_operator.save_wav(f, samplerate, signal, args.output_path))
    )
    pipeline.collect()

if __name__ == '__main__':
    args = argparser.parse()
    main(args)
