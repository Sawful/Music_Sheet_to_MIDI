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


def match(template_image_path, music_sheet_path):

    # Initialise both reference image (with its contour) and approximated image
    template_image_contour, template_image = create_contour(template_image_path)
    music_sheet = cv2.imread(music_sheet_path)

    # Apply grayscale
    template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
    music_sheet = cv2.cvtColor(music_sheet, cv2.COLOR_BGR2GRAY)

    # Create threshold for both template and viewed image
    # template_image = cv2.adaptiveThreshold(~template_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2);
    # music_sheet = cv2.adaptiveThreshold(~music_sheet, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2);

    _, template_image = cv2.threshold(~template_image, 75, 255, 0)
    _, music_sheet = cv2.threshold(~music_sheet, 75, 255, 0)

    # ///

    # Create the images that will use to extract the horizontal and vertical lines
    horizontal = np.copy(music_sheet)
    vertical = np.copy(music_sheet)

    (rows, cols) = horizontal.shape

    horizontalSize = cols / 30
    verticalSize = rows / 30

    # Create structure element for extracting horizontal lines through morphology operations
    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (int(horizontalSize), 1))

    cv2.erode(horizontal, horizontalStructure, horizontal)

    cv2.dilate(horizontal, horizontalStructure, horizontal)

    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, int(verticalSize)))

    cv2.erode(vertical, verticalStructure, vertical)
    cv2.dilate(vertical, verticalStructure, vertical)

    test = cv2.subtract(music_sheet, horizontal)

    cv2.imshow("vertical", test)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # ///

    # corr = cv2.matchTemplate(music_sheet, template_image,
    #                          cv2.TM_CCOEFF_NORMED)
    #
    # # Find the maximum correlation value and its location
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corr)
    #
    # # Calculate the top-left and bottom-right corners of the bounding box
    # top_left = max_loc
    # bottom_right = (top_left[0] + template_image.shape[1], top_left[1] + template_image.shape[0])
    #
    # # Draw a rectangle around the matched region
    # cv2.rectangle(image, top_left, bottom_right, 0, 2)
    #
    # cv2.imshow("Approximate Contour", image)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


bad_apple_sheet_path = 'musicsheet/bad_apple_musicsheet.png'
bad_apple_image = cv2.imread(bad_apple_sheet_path)

noire_img_path = 'solfege/note/noire.png'
noire_contour, noire_img = create_contour(noire_img_path)

match(noire_img_path, bad_apple_sheet_path)
