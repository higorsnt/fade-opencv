import cv2
from fade import fade
from slideshow import show

imagem1 = cv2.imread("../input/eevee.jpg")
imagem2 = cv2.imread("../input/flareon.jpg")

# chamando o responsavel por realizar o fade
fade(imagem1, imagem2)

# mostrando o resultado na tela
show()
