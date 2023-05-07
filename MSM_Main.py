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


def threshold_image(image, thresh_min):

    # converting image into grayscale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # setting threshold of gray image
    _, threshold = cv2.threshold(gray, thresh_min, 255, cv2.THRESH_BINARY)

    return threshold


def create_contour(img_path):

    image = cv2.imread(img_path)

    threshold = threshold_image(image, 200)

    # using a findContours() function
    contours_image, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours_image[1], image


def extract_lines(thresh_img):

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
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
    detected_lines = cv2.morphologyEx(thresh_img, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) <= 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(thresh_img, [c], -1, 255, 1)

    repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
    thresh_img = 255 - cv2.morphologyEx(255 - thresh_img, cv2.MORPH_CLOSE, repair_kernel, iterations=1)

    return ~thresh_img, ~horizontal


def match(template_image_path, music_sheet_path, threshold):

    # Initialise both reference image (with its contour) and approximated image
    template_image_contour, template_image = create_contour(template_image_path)
    music_sheet = cv2.imread(music_sheet_path)

    template_image = threshold_image(~template_image, 75)
    music_sheet = threshold_image(~music_sheet, 75)

    no_line_sheet = extract_lines(music_sheet)[0]

    corr = cv2.matchTemplate(no_line_sheet, template_image,
                             cv2.TM_CCOEFF_NORMED)

    # Store the coordinates of matched area in a numpy array
    loc = np.where(corr >= threshold)
    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        cv2.rectangle(no_line_sheet, pt, (pt[0] + template_image.shape[1], pt[1] + template_image.shape[0]), 255, 1)

    return loc, corr


def sort_location(loc, corr, close_distance):
    if len(loc[0]) > 0:
        note_loc_list_x = [loc[0][0]]
        note_loc_list_y = [loc[1][0]]
        for x, y in zip(loc[0], loc[1]):
            note_counter = 0
            for assigned_x, assigned_y in zip(note_loc_list_x, note_loc_list_y):
                note_counter += 1
                # If close to another already found note
                if assigned_x + close_distance > x > assigned_x - close_distance and assigned_y + close_distance > y > assigned_y - close_distance:

                    if corr[x, y] > corr[assigned_x, assigned_y]:
                        note_loc_list_x[note_loc_list_x.index(assigned_x)] = x
                        note_loc_list_y[note_loc_list_y.index(assigned_y)] = y

                    break

                elif note_counter == len(note_loc_list_x):
                    note_loc_list_x.append(x)
                    note_loc_list_y.append(y)

        note_loc_list = [note_loc_list_x, note_loc_list_y]

        return note_loc_list


def sorted_match(template_image_path, music_sheet_path, threshold):
    # todo: remove useless code
    location, correlation = match(template_image_path, music_sheet_path, threshold)
    sorted_loc = sort_location(location, correlation, 3)

    # Initialise both reference image (with its contour) and approximated image
    template_image_contour, template_image = create_contour(template_image_path)
    music_sheet = cv2.imread(music_sheet_path)

    # Apply grayscale
    template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
    music_sheet = cv2.cvtColor(music_sheet, cv2.COLOR_BGR2GRAY)

    _, template_image = cv2.threshold(~template_image, 75, 255, 0)
    _, music_sheet = cv2.threshold(~music_sheet, 75, 255, 0)

    no_line_sheet = extract_lines(music_sheet)[0]

    if sorted_loc is None:
        return no_line_sheet

    # Draw a rectangle around the matched region.
    for pt in zip(*sorted_loc[::-1]):
        cv2.rectangle(no_line_sheet, pt, (pt[0] + template_image.shape[1], pt[1] + template_image.shape[0]), 255, 1)

    return no_line_sheet

bad_apple_sheet_path = 'musicsheet/bad_apple_musicsheet.png'
bad_apple_image = cv2.imread(bad_apple_sheet_path)
all_my_trial_sheet_path ='musicsheet/all_my_trial_music_sheet.jpg'
all_my_trial_image = cv2.imread(all_my_trial_sheet_path)
boilem_cabbage_down_path ='musicsheet/boilem-cabbage-down-piano-alphanotes-helper.jpg'
boilem_cabbage_down_image = cv2.imread(boilem_cabbage_down_path)

# Initialise note types
noire_img_path = 'solfege/note/noire.png'
ronde_img_path = 'solfege/note/ronde.png'
blanche_img_path = 'solfege/note/blanche.png'
croche_img_path = 'solfege/note/croche.png'
double_croche_img_path = 'solfege/note/double_croche.png'
triple_croche_img_path = 'solfege/note/triple_croche.png'
noire_contour, noire_img = create_contour(noire_img_path)
ronde_contour, ronde_img = create_contour(ronde_img_path)
blanche_contour, blanche_img = create_contour(blanche_img_path)
croche_contour, croche_img = create_contour(croche_img_path)
double_croche_contour, double_croche_img = create_contour(double_croche_img_path)
triple_croche_contour, triple_croche_img = create_contour(triple_croche_img_path)

# display_image("ronde sheet", extract_lines(threshold_image(bad_apple_image, 75))[0])
# display_image("ronde sheet", sorted_match(noire_img_path, bad_apple_sheet_path, 0.63))

# display_image("noire sheet", sorted_match(noire_img_path, bad_apple_sheet_path, 0.63))
# display_image("ronde sheet", sorted_match(ronde_img_path, boilem_cabbage_down_path, 0.63))
# display_image("blanche sheet", sorted_match(blanche_img_path, bad_apple_sheet_path, 0.63))
# display_image("croche sheet", sorted_match(croche_img_path, bad_apple_sheet_path, 0.55))
# display_image("double croche sheet", sorted_match(double_croche_img_path, bad_apple_sheet_path, 0.63))
# display_image("triple croche sheet", sorted_match(triple_croche_img_path, bad_apple_sheet_path, 0.63))
