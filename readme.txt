## first step.
make sure anaconda is installed

## create new environment using environment.yaml with following command.
conda env create -n <env_name> -f environment.yaml

## download all the required DLL from google drive below.
https://drive.google.com/drive/folders/1HimwhHXfF9Fe4R-0t26Nj0zz-TWz82Za

## activate the environment created.
conda activate <env_name>

## testing on the object detection
python main.py