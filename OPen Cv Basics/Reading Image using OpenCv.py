import cv2

img = cv2.imread(r'C:\Users\ritik\Downloads\iron-man-in-marvels-avengers-19-1920x1080.jpg')


cv2.imshow("Iron-Man",img)


cv2.waitKey(0)
cv2.destroyAllWindows()