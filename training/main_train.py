import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

DEFAULT_DARKNET_DIR='C:/darknet-master'
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
THIS_DIR = THIS_DIR.replace(os.sep, '/')

class Train:
    def __init__(self):  
        cfgFileName = 'data/yolov3_custom.cfg'
        modelName = QFileDialog.getOpenFileName(caption='Select Base Model', directory=f'{THIS_DIR}/data/yolov4.conv.137')
        command=f'"{DEFAULT_DARKNET_DIR}/darknet.exe detector train "{THIS_DIR}/data/obj.data" "{THIS_DIR}/{cfgFileName}" "{modelName[0]}" '
        print(command)
        os.system('cmd /k '+command)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    train = Train()
