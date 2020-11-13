from PIL import Image
import requests
from io import BytesIO

def zoomer(image, zoom):
    if type(zoom) != int:
        print('Attention : votre facteur de zoom doit être un nombre entier positif')
    taille = image.size
    taille_z = (taille[0] * zoom, taille[1] * zoom)
    if taille_z[0] < 3000 and taille_z[1] < 3000:
        if image.mode != "RGB" and image.mode != "L":
            print("display_zoom ne fonctionne qu'en mode RGB ou en mode L")
        elif image.mode == "RGB":
            image_z = Image.new("RGB", taille_z, (0,0,0))
            tab = image.load()
            tab_z = image_z.load()
            for x in range(taille_z[0]):
                for y in range(taille_z[1]):
                    tab_z[x,y] = tab[x//zoom, y//zoom]
            return image_z
        elif image.mode == "L":
            image_z = Image.new("L", taille_z, 0)
            tab = image.load()
            tab_z = image_z.load()
            for x in range(taille_z[0]):
                for y in range(taille_z[1]):
                    tab_z[x,y] = tab[x//zoom, y//zoom]
            return image_z        
    else: 
        print("Vous avez exagéré : votre affichage sera trop grand ! Réduire votre zomme, merci :-)")

def ouvrir_image_par_url(url):
    return Image.open(BytesIO(requests.get(url).content))
        