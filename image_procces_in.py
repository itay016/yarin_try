import cv2
import pytesseract
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
filename = 'sf.png'
path='pics/WhatsApp Image 2021-10-31 at 07.59.41.jpeg'
# read the image and get the dimensions
img = cv2.imread(path)
h, w, _ = img.shape # assumes color image

# run tesseract, returning the bounding boxes
boxes = pytesseract.image_to_boxes(img)#use
text = pytesseract.image_to_string(img)
print(pytesseract.image_to_string(img)) #print identified text

# draw the bounding boxes on the image
for b in boxes.splitlines():
    b = b.split()
    cv2.rectangle(img, ((int(b[1]), h - int(b[2]))), ((int(b[3]), h - int(b[4]))), (0, 255, 242), 1)

plt.imshow(img)
print()