from PIL import Image
import os
from pathlib import Path

    
def resizeImage(image, WIDTH, HEIGHT, outputFolder):
    path, filename = os.path.split(image)
    filename, fileExtension = os.path.splitext(filename) # splits the extension from the filename for easier saving and printing

    try: 
        image = Image.open(image) # Open the image, causes an exception if file is not an image
        image = image.resize((WIDTH, HEIGHT)) # Resize the image
        finalFilepath = os.path.join(outputFolder, filename + "_resized" + fileExtension) # builds the path string for the new files
        image.save(finalFilepath)
        print("resizing " + filename) # To show it's working
        
    except IOError: # Exceptions occur when not image file
        print("Skipping non-image file: " + filename)

# Get input for file paths and desired image size
print("Path of folder of images to resize:", end="")
path = input()
print("Width of image desired:", end = "")
width = int(input())
print("Height of image desired:", end = "")
height = int(input())
print("Desired output folder (leave blank to save in same folder):", end = "")
outputFolder = input()
print()

entries = os.scandir(path)
for entry in entries:
    if not outputFolder:
        outputFolder = path
    Path(outputFolder).mkdir(parents=True, exist_ok=True) # Make directory if it doesn't exist
    resizeImage((path + "\\" + entry.name), width, height, outputFolder)
    




