#!/bin/bash
set -e

: "${SPARK_HOME:?Need to set SPARK_HOME}"

$SPARK_HOME/bin/spark-submit \
    --py-files language_detector/preprocessing/eggs.zip \
    --master 'local[4]' \
    language_detector/preprocessing/preprocessing_spark_job.py $@
