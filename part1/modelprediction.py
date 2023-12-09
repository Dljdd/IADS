from imagemodel import imageModel

def makePrediction(image_dir):
    imgModel = imageModel()
    print(imgModel.predict_on_image(image_dir))

# placeholder way to load image
image_dir = "part1/test images/healthy wheat (1).JPG"
makePrediction(image_dir)