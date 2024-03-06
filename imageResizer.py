from PIL import Image
import os

    
def resizeImage(image, WIDTH, HEIGHT, outputFolder):
    filename, fileExtension = os.path.splitext(image) # splits the extension from the filename for easier saving and printing
    # print(filename)
    # print(fileExtension)

    try: 
        image = Image.open(image) # Open the image, causes an exception if file is not an image
        image = image.resize((WIDTH, HEIGHT)) # Resize the image
        finalFilepath = os.path.join(outputFolder, filename + "_resized" + fileExtension) # builds the path string for the new files
        image.save(finalFilepath)
        print("resizing " + filename) # To show it's working
        
    except IOError: # Exceptions occur when not image file
        print("Skipping non-image file: " + filename)


print("Path of folder of images to resize:", end="")
path = input()
print("Width of image desired:", end = "")
width = int(input())
print("Height of image desired:", end = "")
height = int(input())
print("Desired output folder:", end = "")
outputFolder = input()
print()

entries = os.scandir(path)
for entry in entries:
    
    resizeImage((path + "\\" + entry.name), width, height, outputFolder)
    




