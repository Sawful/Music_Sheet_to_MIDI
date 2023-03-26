# Trouver un format d'image - #Definir un template d'image (et convertir si pas le bon template)
# créer une nouvelle image
# Cherche les notes --> Identifier les notes sur l'image
# leur position (comparaison avec des fichiers de notes existantes)
# Renvoyer une image (type MIDI)

from PIL import Image
import cv2
import numpy as np


def create_contour(img_path):

    # reading image
    image = cv2.imread(img_path)

    # converting image into grayscale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # setting threshold of gray image
    _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # using a findContours() function
    contours_image, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours_image[1], image


noire_img_path = 'solfege/note/noire.png'
noire_contour, noire_img = create_contour(noire_img_path)

# cv2.approxPloyDP() function to approximate the shape
approx = cv2.approxPolyDP(
    noire_contour, 0.01 * cv2.arcLength(noire_contour, True), True)

# using drawContours() function
cv2.drawContours(noire_img, [noire_contour], 0, (0, 0, 255), 1)

cv2.imshow('Contour', noire_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# music_sheet_img = Image.open('musicsheet/bad_apple_musicsheet.png')
# music_sheet_img.show()
