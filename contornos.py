import cv2

img = cv2.imread("Fig.png")
#Binarizar la imagen
imgCanny = cv2.Canny(img, 10, 50)
imgCannyBGR = cv2.cvtColor(imgCanny, cv2.COLOR_GRAY2BGR)
#Encontrar contornos
contornos, jerarquia= cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contornos))
print(jerarquia)
#Dibujar contornos encontrados
for i in range(len(contornos)):
    cv2.drawContours(img, contornos, i, (0,255,0),4)
    cv2.imshow("Imagen", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()