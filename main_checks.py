import cv2
import pytesseract
import pandas as pd
import df_main_feches as db_m



def main():
    my_db= db_m.db_matirials()

    img = cv2.imread('pics/WhatsApp Image 2021-10-31 at 07.59.06.jpeg')
    image_checks=my_db.get_word_list('ISOTHIOAZOLINONE')

    ansin,isans = image_check(img,image_checks)
    if ansin:
        print("ok to use")
    else:
        print("Not good")
    #print(text)


def image_check(img,words):
    anses=[] #-1 : word in text , 1 word not in text
    message=""
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    boxes = pytesseract.image_to_boxes(image=img)# use
    text = pytesseract.image_to_string(img)
    if (len(text)<50):
        print('seems to have a probelem please retake')
        message='seems to have a probelem please retake'
        return False,[-1],message
    check_text = text.upper()
    for word_ in words:
        word_=word_.upper()
        if word_ in check_text :
            anses.append(-1)
        else:
            anses.append(1)
    if -1 in anses:
        return False,anses,message
    else:
        return True , anses,message
    pass



if __name__ == "__main__":
    main()