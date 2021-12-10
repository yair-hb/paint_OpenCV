#opciones de dibujo sobre un aimagen usando la libreria opencv2
import cv2
import numpy as np

imagen = 255*np.ones((400,600,3),dtype=np.uint8)

#dibujando lineas sobre la imagen 
cv2.line(imagen,(0,0),(400,300),(120,255,90), 5)
cv2.line(imagen,(300,0),(300, 200), (255,0,0),4)

#dibujando rectangulos sobre la imagen 
cv2.rectangle(imagen,(50,50),(150,300),(255,2,250), 4)
cv2.rectangle(imagen,(350,80),(450,230),(0,0,0), -1)

#dibujando cirulos sobre la imagen 
cv2.circle(imagen, (500,200), 45,(0,0,0), -1)
cv2.circle(imagen, (50,50), 50, (200,200,200), 5)

cv2.imshow('IMAGEN', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()