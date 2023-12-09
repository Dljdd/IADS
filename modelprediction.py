from imagemodel import imageModel

def makePrediction(image_dir):
    imgModel = imageModel()
    print(imgModel.predict_on_image(image_dir))

# placeholder way to load image
image_dir = "test images\healthy wheat (2).JPG"
makePrediction(image_dir)