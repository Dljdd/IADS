import numpy as np
import cv2
from keras.utils import img_to_array
from keras.applications import vgg16
from keras.models import Model
from keras.layers import GlobalAveragePooling2D, Dense

class imageModel:
  def __init__(self) -> None:
    self.all_labels = ['Tomato Early blight leaf', 'Healthy Tomato leaf', 'Tomato leaf late blight', 'Wheat leaf Healthy', 'Wheat leaf septoria', 'Wheat leaf stripe_rust']
    self.image_model = self.initalise_model()

  def initalise_model(self):
    img_rows, img_cols = 224, 224

    vgg = vgg16.VGG16(weights = 'imagenet',
                    include_top = False, # making sure not to take last layer
                    input_shape = (img_rows, img_cols, 3))

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

    # copy relative path and load weights
    image_model.load_weights("/Users/dylanmoraes/Documents/GitHub/IADS/part1/wheat_tomato_disease_prediction_model_weights.h5")

    return image_model

  def convert_image_to_array(self, image_dir):
    try:
      image = cv2.imread(image_dir)
      if image is not None:
        image = cv2.resize(image, (224,224)) 
        image_array =  img_to_array(image)
        image_array = np.array(image_array, dtype = np.float16) / 255
        image_array = image_array.reshape(-1, 224, 224, 3)
        return image_array
      else:
        return np.array([])
    except Exception as e:
      print(f"Error : {e}")
      return None
    
  def predict_on_image(self, inputImageDir):
    inputImage = self.convert_image_to_array(inputImageDir)
    prediction = self.image_model.predict(inputImage)
    return self.all_labels[np.argmax(prediction)]