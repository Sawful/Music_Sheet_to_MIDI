#Trouver un format d'image - #Definir un template d'image (et convertir si pas le bon template)
#créer une nouvelle image
#Cherche les notes --> Identifier les notes sur l'image + leur position (comparaison avec des fichiers de notes existantes)
#Renvoyer une image (type MIDI)
#
from PIL import Image

music_sheet_img = Image.open('musicsheet/bad_apple_musicsheet.png')
music_sheet_img.show()