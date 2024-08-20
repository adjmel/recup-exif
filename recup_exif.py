# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recup_exif.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: madjogou					                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/20 20:03:31 by madjogou          #+#    #+#              #
#    Updated: 2024/08/20 20:04:13 by melissaadjogo    ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image
from PIL.ExifTags import TAGS

def extract_exif(image_path):
    # Ouvre l'image et accède aux métadonnées EXIF
    image = Image.open(image_path)
    exif_data = image._getexif()

    # Si l'image ne contient pas de données EXIF, retourne un message approprié
    if not exif_data:
        return "Aucune donnée EXIF trouvée."

    # Dictionnaire pour stocker les métadonnées EXIF
    exif_info = {}

    # Parcours des tags EXIF et stockage dans le dictionnaire exif_info
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        exif_info[tag_name] = value

    return exif_info

# Demander à l'utilisateur de saisir le chemin de l'image
image_path = input("Veuillez entrer le chemin de l'image: ")

# Extraire les informations EXIF
exif_info = extract_exif(image_path)

# Afficher les informations EXIF extraites
if isinstance(exif_info, str):
    print(exif_info)
else:
    for key, value in exif_info.items():
        print(f"{key}: {value}")

