#se muestran las distintas formas de escribir textosobre una imagen
import cv2
import numpy as np

imagen = 255*np.ones((500,700), dtype=np.uint8)

letra = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(imagen, 'PRACTICANDO CON OPEN CV', (10,30), letra,1,(0,255,255), 2, cv2.LINE_AA)

cv2.imshow('imagen de prueba', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

