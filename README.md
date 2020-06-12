# seg-platform
A panoptic segmentation web platform.
![Page](https://github.com/txfs19260817/seg-platform/blob/master/docs/1.png)

## Features
- RESTful API backend written in Flask, Python
- Vue.js-based frontend
- Support inference on either a single image or mulitple images
- Support both aerial/satellite and scene panoptic image segmentation

## Project setup
Download weight files from [here](https://drive.google.com/file/d/1U3jyHGrWLbaPvpW1sh2VSe86ZaIvnz2q/view?usp=sharing) and extract under `seg-platform/server/model/weight`. Then, 
```
# Backend setup
cd seg-platform/server
# see Acknowledgement section for more environment setup instructions.
pip install -r requirements.txt
python app.py

# Frontend setup
cd ..
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Acknowledgement
The model deployed in backend is based on https://github.com/mapillary/seamseg . Please check this repository for more requirements and setup instructions.