import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# get the image
img = cv2.imread('text_and_number_example.png')

# convert from BGR to RGB color
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# print(pytesseract.image_to_string(img))
#
# # Detecting Characters
# # print(pytesseract.image_to_boxes(img))
# hImg,wImg,_ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     print(b)
#     b = b.split(' ')
#     print(b)    # in here data into list, so we can get the data
#     x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])    # basicaly string, and voncert to int
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)  # 2 is thickness
#     cv2.putText(img, b[0], (x,hImg-y+25), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255))



# # Detecting Words
# # print(pytesseract.image_to_boxes(img))
# hImg,wImg,_ = img.shape
# boxes = pytesseract.image_to_data(img)
# print(boxes)
# for x,b in enumerate(boxes.splitlines()):
#     # print(b)
#     if x != 0:  # jangan ambil headernya
#         b = b.split()
#         print(b)    # in here data into list, so we can get the data
#         if len(b) == 12:    # soalnya ada 12 data
#             x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])    # basicaly string, and voncert to int
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),2)  # 2 is thickness
#             cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255))


# # Detecting Numbers
# hImg,wImg,_ = img.shape
# cong = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_data(img, config=cong)
# print(boxes)
# for x,b in enumerate(boxes.splitlines()):
#     # print(b)
#     if x != 0:  # jangan ambil headernya
#         b = b.split()
#         print(b)    # in here data into list, so we can get the data
#         if len(b) == 12:    # soalnya ada 12 data
#             x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])    # basicaly string, and voncert to int
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),2)  # 2 is thickness
#             cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255))

# Detecting Characters
hImg,wImg,_ = img.shape
cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img, config=cong)
print(boxes)
for b in boxes.splitlines():
    # print(b)
    b = b.split(' ')
    print(b)    # in here data into list, so we can get the data
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])  # basicaly string, and voncert to int
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)  # 2 is thickness
    cv2.putText(img, b[0], (x,hImg-y+25), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255))

cv2.imshow('Hasil', img)
cv2.waitKey(0)
