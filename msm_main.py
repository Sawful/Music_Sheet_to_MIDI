# from PIL import Image
import cv2
import numpy as np


def display_image(window_name, image):
    """INPUT:
    window_name(str): name of the window display of the image.
    image(ndarray): image to display

    Shows the inputted image with opencv's .imshow()
    """

    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def threshold_image(image, thresh_min):
    """INPUT:
    image(ndarray): image to threshold
    thresh_min(float): the thresh amount, if part of the image isn't shown, decrease this value.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, thresh_min, 255, cv2.THRESH_BINARY)

    return threshold


def create_contour(img_path):
    """Returns a list with the contour ([0]) and ndarray ([1]) of the image referenced by its path."""
    image = cv2.imread(img_path)

    threshold = threshold_image(image, 200)

    # using a findContours() function
    contours_image, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    return contours_image[1], image


def extract_lines(thresh_img):
    """Removes horizontal lines of a threshold image"""
    # Create the images that will use to extract the horizontal and vertical lines
    horizontal = np.copy(thresh_img)
    vertical = np.copy(thresh_img)

    (rows, cols) = horizontal.shape[0], horizontal.shape[1]

    horizontal_size = cols // 30
    vertical_size = rows // 30

    # Create structure element for extracting horizontal lines through morphology operations
    horizontal_structure = cv2.getStructuringElement(
        cv2.MORPH_RECT, (int(horizontal_size), 1)
    )

    cv2.erode(horizontal, horizontal_structure, horizontal)

    cv2.dilate(horizontal, horizontal_structure, horizontal)

    # Create structure element for extracting vertical lines through morphology operations
    vertical_structure = cv2.getStructuringElement(
        cv2.MORPH_RECT, (1, int(vertical_size))
    )

    cv2.erode(vertical, vertical_structure, vertical)
    cv2.dilate(vertical, vertical_structure, vertical)

    # Remove horizontal
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
    detected_lines = cv2.morphologyEx(
        thresh_img, cv2.MORPH_OPEN, horizontal_kernel, iterations=2
    )
    cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) <= 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(thresh_img, [c], -1, 255, 1)

    repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
    thresh_img = 255 - cv2.morphologyEx(
        255 - thresh_img, cv2.MORPH_CLOSE, repair_kernel, iterations=1
    )

    return ~thresh_img, ~horizontal


def match(template_image_path, music_sheet_path, threshold):
    # Initialise both reference image (with its contour) and approximated image
    template_image_contour, template_image = create_contour(template_image_path)
    music_sheet = cv2.imread(music_sheet_path)

    template_image = threshold_image(~template_image, 75)
    music_sheet = threshold_image(~music_sheet, 75)

    no_line_sheet = extract_lines(music_sheet)[0]

    corr = cv2.matchTemplate(no_line_sheet, template_image, cv2.TM_CCOEFF_NORMED)

    # Store the coordinates of matched area in a numpy array
    loc = np.where(corr >= threshold)
    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        cv2.rectangle(
            no_line_sheet,
            pt,
            (pt[0] + template_image.shape[1], pt[1] + template_image.shape[0]),
            255,
            1,
        )

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
                if (
                    assigned_x + close_distance > x > assigned_x - close_distance
                    and assigned_y + close_distance > y > assigned_y - close_distance
                ):
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
    location, correlation = match(template_image_path, music_sheet_path, threshold)
    sorted_loc = sort_location(location, correlation, 3)

    # Initialise both reference image (with its contour) and approximated image
    template_image_contour, template_image = create_contour(template_image_path)
    music_sheet = cv2.imread(music_sheet_path)

    # Apply threshold
    threshold_image(template_image, threshold)
    threshold_image(music_sheet, threshold)

    no_line_sheet = extract_lines(music_sheet)[0]

    if sorted_loc is None:
        return no_line_sheet

    # Draw a rectangle around the matched region.
    for pt in zip(*sorted_loc[::-1]):
        cv2.rectangle(
            no_line_sheet,
            pt,
            (pt[0] + template_image.shape[1], pt[1] + template_image.shape[0]),
            255,
            1,
        )

    return no_line_sheet


bad_apple_sheet_path = "musicsheet/bad_apple_musicsheet.png"
bad_apple_image = cv2.imread(bad_apple_sheet_path)

# Initialise note types
whole_img_path = "music_theory/note/whole.png"
half_img_path = "music_theory/note/half.png"
quarter_img_path = "music_theory/note/quarter.png"
eighth_img_path = "music_theory/note/eighth.png"
sixteenth_img_path = "music_theory/note/sixteenth.png"
thirty_second_img_path = "music_theory/note/thirty_second.png"
# Initialise note contours
whole_contour, whole_img = create_contour(whole_img_path)
half_contour, half_img = create_contour(half_img_path)
quarter_contour, quarter_img = create_contour(quarter_img_path)
eighth_contour, eighth_img = create_contour(eighth_img_path)
sixteenth_contour, sixteenth_img = create_contour(sixteenth_img_path)
thirty_second_contour, thirty_second_img = create_contour(thirty_second_img_path)

# Display the music sheet
display_image(
    "quarter note Bad Apple sheet",
    sorted_match(quarter_img_path, bad_apple_sheet_path, 0.63),
)
