import numpy as np
import yaml
import networkinput
import argparse
import importlib

def predict(args):
    config = yaml.load(file(args.config))

    network_module = "network.instances.{0}".format(config["NET"])
    network_generator = getattr(importlib.import_module(network_module), "generate")

    net = network_generator(config["INPUT_SHAPE"], config["OUTPUT_SHAPE"][0])

    image = networkinput.read_png(args.image_path, "L")
    net.predict(args.model_path, np.expand_dims(image, axis=0))

if __name__ == "__main__":  

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", default="config.yaml", help="Path to config file")
    parser.add_argument('--image', dest='image_path', help='Path to image file', required=True)
    parser.add_argument('--model', dest='model_path', required=True, help='Path to saved tensorflow model')

    args = parser.parse_args()

    predict(args)
