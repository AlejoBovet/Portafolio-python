

import cv2

path= r'C:\Users\alej1\OneDrive\Escritorio\Informatica\python\reconocimiento_facial\imagen1.jpg'

imagen= cv2.imread(path)
grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
contorno,jerarquia= cv2.findContours(umbral, cv2.RETR_LIST, cv2.chain_prox_app)
cv2.drawContours(imagen, contorno,1(251, 60, 40), 4 )

#Mostrar
cv2.imshow('soy gris',grises)
cv2.imshow('normal', imagen)
cv2.imshow('imagen umbral', umbral)
"""sirve para congelar la imagen"""
cv2.waitKey(0)# el "0" se utiliza para imagenes estaticas en cambio el "1" se utuliza para videos o uso de la camara
cv2.destroyAllWindows()

