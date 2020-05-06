import argparse
import io
import os
import shutil

from PIL import Image
from flask import Flask, request
from flask_cors import *

from model import predict as get_prediction

# app settings
app = Flask(__name__)
CORS(app, supports_credentials=True)

# args
parser = argparse.ArgumentParser(description="Panoptic testing script")
parser.add_argument("--model", type=str, default="./model/weight/model_best.pth.tar", help="Path to model weight file")
parser.add_argument("--data", type=str, default="./inputs", help="Path to input data")
args = parser.parse_args()


def set_dir(filepath):
    """
    Create a folder if the given path does not exist.
    Otherwise remove and recreate the folder.
    :param filepath: path
    :return:
    """
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    else:
        shutil.rmtree(filepath)
        os.mkdir(filepath)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # open and save the uploaded image
        file = request.files['file']
        img_bytes = file.read()
        input_image = Image.open(io.BytesIO(img_bytes))
        set_dir(args.data)
        input_image.save(os.path.join(args.data, "input.png"))

        return get_prediction(args)


if __name__ == '__main__':
    set_dir(args.data)
    app.run()
