import os
import time
import cv2
import numpy as np
import darknet

class darknet_detect(object):
    def __init__(self):
        super(darknet_detect,self).__init__()

        config_file = "./cfg/yolov3.cfg"
        data_file = "./cfg/coco.data"
        weights = "yolov3.weights"
        batch_size=1
        network, class_names, class_colors = darknet.load_network(config_file,data_file,weights,batch_size)
        width = darknet.network_width(network)
        height = darknet.network_height(network)
        darknet_image = darknet.make_image(width, height, 3)
        darknet.detect_image(network, class_names, darknet_image, thresh=0.25) ##Predict first dummy##
        
        self.img_dir = "./image"
        self.list_images = os.listdir(self.img_dir)  

        for filename in self.list_images:
            t = time.time() 
            image = cv2.imread(os.path.join(self.img_dir,filename))
            # image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image_resized = cv2.resize(image, (width, height),
                                       interpolation=cv2.INTER_LINEAR)

            darknet.copy_image_from_bytes(darknet_image, image_resized.tobytes())
            bboxes = darknet.detect_image(network, class_names, darknet_image, thresh=0.25)

            image = darknet.draw_boxes(bboxes, image_resized, class_colors)

            cv2.imshow('image', image)
            print(time.time()-t)

            cv2.waitKey(0)


if __name__ == '__main__':
    #a = docker_detect()
    b = darknet_detect()

