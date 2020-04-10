import os
import argparse
from fastai.vision import *
import pydicom

# load the model

def initialize_model(model_path="."):
    """
    Initialize the model from disk
    By default, the model is exported to './export.pkl'

    return the model
    """
    return load_learner(model_path)

def run_inference(input_scan, model_path=".", precision=4):
    """
    Run the infered model
    inputs:
    - input_scan: input x-ray image
    - model path to load
    - precision decimals

    output:
    - output probability for COVID
    """

    # load the learner
    learn = initialize_model(model_path)

    pred = learn.predict(open_image(input_scan))[2][0].numpy()
    return pred


if __name__ == "__main__":
    """
    COVID-19 x-ray classification
    resnet50 two stage model
    """
    parser = argparse.ArgumentParser(description='COVID-19 x-ray classification')
    parser.add_argument('--input_scan', default=None, help='input_image')
    opt = parser.parse_args()

    prob = run_inference(opt.input_scan)

    scan_name = os.path.split(opt.input_scan)[0]
    print('--------------------------------------------------')
    print('SCAN: {0} ----> PROB: {1:.2f} %'.format(scan_name, prob * 100))
    print('--------------------------------------------------')
