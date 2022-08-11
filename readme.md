# For Inferencing:

1. First step.
make sure anaconda and python > 3.8 is installed

2. Create new environment using environment.yaml with following command.
conda env create -n <env_name> -f environment.yaml

3. Download all the required DLL from google drive below and put all of them to current folder as below.
https://drive.google.com/drive/folders/1HimwhHXfF9Fe4R-0t26Nj0zz-TWz82Za
- Darknet-Easy-Installation\
  - data\
  - cfg\
  - image\
  - training\
  - darknet.py
  - environment.yaml
  - main.py
  - readme.txt
  - cudnn_adv_infer64_8.dll
  - cudnn_adv_train64_8.dll
  - ...

4. Activate the environment created.
activate your environment with cuda installed
conda activate <env_name>
cd to folder path

5. Testing on the object detection
python main.py

Enjoy your Darknet YOLO object detection!

# For model training:
1. Please download the darknet-master.rar from the link below, extract and put in C-drive:
https://drive.google.com/drive/folders/1BPMs6rr0uEXY6Q_DrlUJ9uZIhtKVB1H_?usp=sharing

- C:\\
  - darknet-master
  
2. Please download the pre-trained model yolov4.conv.137 from link below and put in data folder:
https://drive.google.com/drive/folders/1Ikti48wHULfJ-Rfi4s6_Ibf68PUJQfyZ?usp=sharing

- training\
  - data\
    - anchors\
    - code.txt
    - obj.data
    - obj.names
    - test.txt
    - train.txt
    - yolov3_custom.cfg
    - yolov4.conv.137

3. test the model training using following command:
activate your environment with cuda installed
conda activate <env_name>
cd to folder path
python main_train.py

4. prepare the dataset according to guidance of AlexeyAb:
https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects

Enjoy training your own custom object detection!

## If cuda error, please update your geforce driver to the latest version
