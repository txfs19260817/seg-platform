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
parser.add_argument(
    "--model",
    type=str,
    default="./model/weight/iSAID/model_best.pth.tar",
    help="Path to model weight file"
)
parser.add_argument(
    "--config",
    type=str,
    default="./model/weight/iSAID/iSAID_r50.ini",
    help="Path to config file"
)
parser.add_argument(
    "--meta",
    type=str,
    default="./model/weight/iSAID/metadata.bin",
    help="Path to metadata file"
)
parser.add_argument(
    "--data",
    type=str,
    default="./inputs",
    help="Path to input data"
)
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
    """
    router to get prediction.
    :return: base64 png
    """
    if request.method == 'POST':

        # reload args according to seg task type
        seg_type = request.form["type"]
        if "vista" in seg_type:
            args.model = "./model/weight/vistas/seamseg_r50_vistas.tar"
            args.config = "./model/weight/vistas/config.ini"
            args.meta = "./model/weight/vistas/metadata.bin"
        else:
            args.model = "./model/weight/iSAID/model_best.pth.tar"
            args.config = "./model/weight/iSAID/iSAID_r50.ini"
            args.meta = "./model/weight/iSAID/metadata.bin"
        args.data = "./inputs"

        # open and save the uploaded image
        file = request.files['file']
        img_bytes = file.read()
        input_image = Image.open(io.BytesIO(img_bytes))
        set_dir(args.data)
        input_image.save(os.path.join(args.data, "input.png"))

        # send the prediction to frontend
        return get_prediction(args)


if __name__ == '__main__':
    set_dir(args.data)
    app.run()
