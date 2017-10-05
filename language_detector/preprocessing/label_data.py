import os
import random
import csv
from util import argparser, filecollector

def label_data(src_path, dest_path):
    src_paths = [os.path.join(src_path, name) for name in os.listdir(src_path)
                 if os.path.isdir(os.path.join(src_path, name))]
    train = []
    test = []
    label = 0
    for src_path in src_paths:
        train_paths, test_paths = split_data(src_path)
        train += [[path, label] for path in train_paths]
        test += [[path, label] for path in test_paths]
        label += 1
    random.shuffle(train)
    random.shuffle(test)
    write_to_csv(train, os.path.join(dest_path, 'train.csv'))
    write_to_csv(test, os.path.join(dest_path, 'test.csv'))

def split_data(src_path):
    paths = filecollector.collect(src_path, file_extension='png')
    random.shuffle(paths)
    split_index = int(0.8 * len(paths))
    train_paths = paths[:split_index]
    test_paths = paths[split_index:]
    return train_paths, test_paths

def write_to_csv(data, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    args = argparser.parse()
    label_data(args.input_path, args.output_path)
