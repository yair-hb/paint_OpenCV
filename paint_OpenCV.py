#opciones de dibujo sobre un aimagen usando la libreria opencv2
import cv2
import numpy as np

imagen = 255*np.ones((400,600,3),dtype=np.uint8)

cv2.imshow('IMAGEN', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()