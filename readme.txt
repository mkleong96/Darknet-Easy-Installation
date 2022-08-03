1. First step.
make sure anaconda and python > 3.8 is installed

2. Create new environment using environment.yaml with following command.
conda env create -n <env_name> -f environment.yaml

3. Download all the required DLL from google drive below and put all of them to current folder.
https://drive.google.com/drive/folders/1HimwhHXfF9Fe4R-0t26Nj0zz-TWz82Za
- Darknet-Easy-Installation\
  - data\
  - cfg\
  - sample\
  - darknet.py
  - environment.yaml
  - main.py
  - readme.txt
  - cudnn_adv_infer64_8.dll
  - ...

4. Activate the environment created.
cd to folder path
conda activate <env_name>

5. Testing on the object detection
python main.py

Enjoy your Darknet YOLO object detection!

## If cuda error, please update your geforce driver to the latest version
