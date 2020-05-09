import argparse
import io
import os

from PIL import Image
from flask import Flask, request, send_file, abort, Response
from flask_cors import *

from model import predict as get_prediction
from utils import set_dir, check_and_save_img

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
    default="inputs",
    help="Path to input data"
)
parser.add_argument(
    "--output",
    type=str,
    default="outputs",
    help="Path to output data"
)
args = parser.parse_args()


@app.route('/predict', methods=['POST'])
def predict():
    """
    router to get prediction.
    :return: base64 png
    """
    if request.method == 'POST':

        # reload args according to seg task type
        seg_type = request.args.get("type")
        multiple = request.args.get("multiple") != '0'
        if seg_type is not None and "vista" in seg_type:
            args.model = "./model/weight/vistas/seamseg_r50_vistas.tar"
            args.config = "./model/weight/vistas/config.ini"
            args.meta = "./model/weight/vistas/metadata.bin"
        else:
            args.model = "./model/weight/iSAID/model_best.pth.tar"
            args.config = "./model/weight/iSAID/iSAID_r50.ini"
            args.meta = "./model/weight/iSAID/metadata.bin"

        # mkdir if not exist
        set_dir(args.data)

        # open and save the uploaded image
        if multiple:
            set_dir(args.output)
            for i in range(len(request.files)):
                file = request.files['file{}'.format(i)]
                not_valid = check_and_save_img(file, os.path.join(args.data, "input{}.png".format(i)))
                if not_valid:
                    abort(Response(not_valid))
        else:
            file = request.files['file']
            not_valid = check_and_save_img(file, os.path.join(args.data, "input.png"))
            if not_valid:
                abort(Response(not_valid))

        # send the prediction to frontend
        pred = get_prediction(args, multiple)
        zipfile_name = args.output + ".zip"
        return pred if not multiple else send_file(zipfile_name, mimetype="application/zip", as_attachment=True,
                                                   attachment_filename=zipfile_name)


if __name__ == '__main__':
    app.run()
