# Trouver un format d'image - #Definir un template d'image (et convertir si pas le bon template)
# créer une nouvelle image
# Cherche les notes --> Identifier les notes sur l'image
# leur position (comparaison avec des fichiers de notes existantes)
# Renvoyer une image (type MIDI)

from PIL import Image
import cv2

import numpy as np


def display_image(window_name, img):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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


def remove_lines(thresh_img):

    """
    thresh_img: threshold image in which you want to remove the lines.
    """
    # Create the images that will use to extract the horizontal and vertical lines
    horizontal = np.copy(thresh_img)
    vertical = np.copy(thresh_img)

    (rows, cols) = horizontal.shape

    horizontalSize = cols // 30
    verticalSize = rows // 30

    # Create structure element for extracting horizontal lines through morphology operations
    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (int(horizontalSize), 1))

    cv2.erode(horizontal, horizontalStructure, horizontal)

    cv2.dilate(horizontal, horizontalStructure, horizontal)

    # Create structure element for extracting vertical lines through morphology operations
    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, int(verticalSize)))

    cv2.erode(vertical, verticalStructure, vertical)
    cv2.dilate(vertical, verticalStructure, vertical)

    # Remove horizontal
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
    detected_lines = cv2.morphologyEx(thresh_img, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) <= 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(thresh_img, [c], -1, 255, 1)

    repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
    thresh_img = 255 - cv2.morphologyEx(255 - thresh_img, cv2.MORPH_CLOSE, repair_kernel, iterations=1)

    return thresh_img


def match(template_image_path, music_sheet_path):

    # Initialise both reference image (with its contour) and approximated image
    template_image_contour, template_image = create_contour(template_image_path)
    music_sheet = cv2.imread(music_sheet_path)

    # Apply grayscale
    template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
    music_sheet = cv2.cvtColor(music_sheet, cv2.COLOR_BGR2GRAY)

    _, template_image = cv2.threshold(~template_image, 75, 255, 0)
    _, music_sheet = cv2.threshold(~music_sheet, 75, 255, 0)

    no_line_sheet = remove_lines(music_sheet)

    corr = cv2.matchTemplate(no_line_sheet, template_image,
                             cv2.TM_CCOEFF_NORMED)

    print(corr[322][403])

    # Specify a threshold
    threshold = 0.63

    # Store the coordinates of matched area in a numpy array
    loc = np.where(corr >= threshold)
    print(loc)
    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        cv2.rectangle(no_line_sheet, pt, (pt[0] + template_image.shape[1], pt[1] + template_image.shape[0]), 255, 1)

    display_image("no line sheet", no_line_sheet)


bad_apple_sheet_path = 'musicsheet/bad_apple_musicsheet.png'
bad_apple_image = cv2.imread(bad_apple_sheet_path)

noire_img_path = 'solfege/note/noire.png'
noire_contour, noire_img = create_contour(noire_img_path)

match(noire_img_path, bad_apple_sheet_path)
