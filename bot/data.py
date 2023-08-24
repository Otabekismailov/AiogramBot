# import cv2
# import pytesseract
#
# # Open the image file
# image_path = '../media/image.jpg'
# image = cv2.imread(image_path)
#
# # Convert the image to text using Tesseract OCR
# try:
#     text = pytesseract.image_to_string(image)
#
#     print(text)
# except Exception as e:
#     print(f"Error: {e}")
#


# import the following libraries
# will convert the image to text string
import pytesseract

# adds image processing capabilities
from PIL import Image

# converts the text to speech
import pyttsx3

# translates into the mentioned language
from googletrans import Translator

# opening an image from the source path
img = Image.open('../media/image.jpg')

# describes image format in the output
print(img)
# path where the tesseract module is installed
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('abc.txt', mode='w') as file:
    file.write(result)
    print(result)

p = Translator()
# translates the text into german language
k = p.translate(result, dest='russian')
print(k)
engine = pyttsx3.init()

# an audio will be played which speaks the test if pyttsx3 recognizes it
engine.say(k)
engine.runAndWait()
