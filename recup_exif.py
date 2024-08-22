# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recup_exif.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: madjogou                                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/20 20:03:31 by madjogou          #+#    #+#              #
#    Updated: 2024/08/20 20:04:13 by madjogou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image, ExifTags, UnidentifiedImageError

def extract_exif(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if not exif_data:
            return "Aucune donnée EXIF trouvée."

        exif_info = {}
        for tag, value in exif_data.items():
            tag_name = ExifTags.TAGS.get(tag, tag)
            exif_info[tag_name] = value
        return exif_info

    except FileNotFoundError:
        return "Erreur : Le fichier spécifié n'a pas été trouvé."
    except Exception as e:
        return f"Erreur inattendue : {str(e)}"

image_path = input("Veuillez entrer le chemin de l'image: ")
exif_info = extract_exif(image_path)

if isinstance(exif_info, str):
    print(exif_info)
else:
    for key, value in exif_info.items():
        print(f"{key}: {value}")


