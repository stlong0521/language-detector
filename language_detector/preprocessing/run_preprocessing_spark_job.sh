#!/bin/bash
set -e

: "${SPARK_HOME:?Need to set SPARK_HOME}"

$SPARK_HOME/bin/run-example SparkPi 10
