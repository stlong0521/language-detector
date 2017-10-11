import yaml
import networkinput
import argparse
import importlib

def evaluate(args):
    config = yaml.load(file(args.config))

    network_module = "network.instances.{0}".format(config["NET"])
    network_generator = getattr(importlib.import_module(network_module), "generate")

    net = network_generator(config["INPUT_SHAPE"], config["OUTPUT_SHAPE"][0])

    training_set = networkinput.CSVInput(config['TRAINING_DATA'], config['INPUT_SHAPE'], config['OUTPUT_SHAPE'][0], mode="L")
    test_set = networkinput.CSVInput(config['TEST_DATA'], config['INPUT_SHAPE'], config['OUTPUT_SHAPE'][0], mode="L")

    net.set_training_input(training_set, test_set)
    net.load_and_evaluate(args.model_path, config["BATCH_SIZE"])

if __name__ == "__main__":  

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", default="config.yaml", help="Path to config file")
    parser.add_argument('--model', dest='model_path', required=True, help='Path to saved tensorflow model')
    args = parser.parse_args()

    evaluate(args)
