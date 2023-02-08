import cv2
import pytesseract

#BEFORE RUN MAKE SURE YOU HAVE EMPTIED THE WHOLE FILE NAMED tmp.txt

with open("tmp.txt", "a") as f:
    #Here we have set the reader to scan the pages from 65 to 510, We can change this reading criteria by changing the values in the for loop bellow
    for i in range(65, 511):
        # Load an image
        img = cv2.imread("page"+str(i)+".jpg")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # For Printing the data that is been identified
        txt = pytesseract.image_to_string(img)
        txt +="\n"
        f.write(txt)