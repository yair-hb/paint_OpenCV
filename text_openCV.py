#se muestran las distintas formas de escribir textosobre una imagen
import cv2
import numpy as np

imagen = 255*np.ones((500,700,3), dtype=np.uint8)

#puedes especificar la tipografia 
letra = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(imagen, 'PRACTICANDO CON OPEN CV', (10,30), letra,1,(0,255,255), 2, cv2.LINE_AA)
#puedes especificar la tipografia con el codigo de cada una 
FONT_HERSHEY_SIMPLEX = 0
FONT_HERSHEY_PLAIN = 1
FONT_HERSHEY_DUPLEX = 2
FONT_HERSHEY_COMPLEX = 3
FONT_HERSHEY_TRIPLEX = 4
FONT_HERSHEY_COMPLEX_SMALL = 5
FONT_HERSHEY_SCRIPT_SIMPLEX = 6
FONT_HERSHEY_SCRIPT_COMPLEX = 7

cv2.putText(imagen, 'TEXTO DE PRUEBA', (10,60), 1,1,(255,0,0),2)
cv2.putText(imagen, 'TEXTO DE PRUEBA', (10,90), 2,1,(255,100,0),2)
cv2.putText(imagen, 'TEXTO DE PRUEBA', (10,120),3,1,(255,250,0),2)
cv2.putText(imagen, 'TEXTO DE PRUEBA', (10,150), 4,1, (255,0,255),2)
cv2.putText(imagen, 'TEXTO DE PRUEBA', (10,180), 5,1, (255,0,255),2)
cv2.putText(imagen, 'TEXTO DE PRUEBA', (10,210), 6,1, (0,255,200), 2)
cv2.putText(imagen, 'TEXTO DE PRUEBA FINAL', (10,240), 7,1,(100,100,100),2)


cv2.imshow('imagen de prueba', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

