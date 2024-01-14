# Show images 
import PIL
from PIL import Image


#images path

dog = Image.open(img_folder,"Arun-new-aadhar.jpg")#image path

#ask user input
imagename = input("Which animal you want to see?" )
print (imagename)

if imagename == "dog":
    dog.show()
else:
    print ("No image found")
