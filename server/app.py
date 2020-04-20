import io
import json
import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
import base64
from flask import Flask, jsonify, request
from flask_cors import *


app = Flask(__name__)
CORS(app, supports_credentials=True)

model = torch.hub.load('pytorch/vision:v0.5.0', 'deeplabv3_resnet101', pretrained=True)
model.eval()

# create a color pallette, selecting a color for each class
palette = torch.tensor([2 ** 25 - 1, 2 ** 15 - 1, 2 ** 21 - 1])
colors = torch.as_tensor([i for i in range(21)])[:, None] * palette
colors = (colors % 255).numpy().astype("uint8")

def transform_image(image):
    my_transforms = transforms.Compose([
                        transforms.ToTensor(),
                        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                    ])
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    # read image from bytes
    input_image = Image.open(io.BytesIO(image_bytes))

    # transform
    input_batch = transform_image(input_image)
    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')
    with torch.no_grad():
        output = model(input_batch)['out'][0]
    output_predictions = output.argmax(0)

    # plot the semantic segmentation predictions of 21 classes in each color
    img = Image.fromarray(output_predictions.byte().cpu().numpy()).resize(input_image.size)
    img.putpalette(colors)

    # create file-object in memory
    file_object = io.BytesIO()

    # write PNG in file-object
    img.save(file_object, 'PNG')

    # convert bytes to base64
    return base64.b64encode(file_object.getvalue()).decode()


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        return get_prediction(image_bytes=img_bytes)


if __name__ == '__main__':
    app.run()
