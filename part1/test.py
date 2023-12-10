import numpy as np
import cv2
from keras.utils import img_to_array
from keras.applications import vgg16
from keras.models import Model
from keras.layers import GlobalAveragePooling2D, Dense


img_rows, img_cols = 224, 224

vgg = vgg16.VGG16(weights = 'imagenet', include_top = False, input_shape = (img_rows, img_cols, 3))

# dont keep layers of pretrained model as trainable 
for layer in vgg.layers:
	layer.trainable = False

def lw(bottom_model, num_classes):
    top_model = bottom_model.output
    top_model = GlobalAveragePooling2D()(top_model)
    top_model = Dense(256,activation='relu')(top_model)
    top_model = Dense(128,activation='relu')(top_model)
    top_model = Dense(96,activation='relu')(top_model)
    top_model = Dense(64,activation='relu')(top_model)
    top_model = Dense(num_classes,activation='softmax')(top_model)
    return top_model

num_classes = 6
FC_Head = lw(vgg, num_classes)
image_model = Model(inputs = vgg.input, outputs = FC_Head)