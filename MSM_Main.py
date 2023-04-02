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


def approximate(reference_image_path, approximated_image_path):
    # initialise a note counter
    note_count = 0
    # Initialise both reference image (with its contour) and approximated image
    reference_image_contour, reference_image = create_contour(reference_image_path)
    approximated_image = create_contour(approximated_image_path)[1]
    # Get image dimensions for both images
    reference_dimensions = reference_image.shape
    image_dimensions = approximated_image.shape
    # Approximate contour for the reference image
    approx_ref = cv2.approxPolyDP(
        reference_image_contour, 0.01 * cv2.arcLength(reference_image_contour, True), True)
    # Scans whole image
    for y in range(image_dimensions[0] - reference_dimensions[0]):
        for x in range(image_dimensions[1] - reference_dimensions[1]):
            # Define cropped image
            cropped_image = approximated_image[x:(x+reference_dimensions[1]), y:(y+reference_dimensions[0])]
            # Create a contour for each cropped image
            gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
            _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
            contours_cropped, _ = cv2.findContours(
                threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            approx = cv2.approxPolyDP(contours_cropped[0], 0.01 * cv2.arcLength(contours_cropped[0], True), True)
            # Detect contour and compare if same as reference
            if len(approx) == len(approx_ref):
                print("noire")
                note_count += 1
    # How many notes are there?
    print(note_count)

noire_img_path = 'solfege/note/noire.png'
noire_contour, noire_img = create_contour(noire_img_path)
bad_apple_sheet_path = 'musicsheet/bad_apple_musicsheet.png'
approximate(noire_img_path, bad_apple_sheet_path)


# cv2.approxPloyDP() function to approximate the shape
# approx = cv2.approxPolyDP(
#     noire_contour, 0.01 * cv2.arcLength(noire_contour, True), True)

# using drawContours() function
cv2.drawContours(noire_img, [noire_contour], 0, (0, 0, 255), 1)

# cv2.imshow('Contour', noire_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# music_sheet_img = Image.open('musicsheet/bad_apple_musicsheet.png')
# music_sheet_img.show()
