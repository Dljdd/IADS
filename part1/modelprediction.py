from part1.imagemodel import imageModel
# import ssl 
# ssl._create_default_https_context = ssl._create_unverified_context

def makePrediction(image_dir):
    imgModel = imageModel()
    print(imgModel.predict_on_image(image_dir))

# placeholder way to load image
image_dir = r"part1/test images"
makePrediction(image_dir)