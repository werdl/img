import openai
import shutil
import requests,turtle
from PIL import Image
import os
key = os.environ.get('OPENAI_API')
openai.api_key=key
f=True
while f:
    try:
        option=int(input("""
0 - Generated by DALL-E
1 - Written in Python turtle

"""))
        f=False
    except:
        f=True
if not option:
    eye=input("Eye color? ").lower()
    hair=input("Hair color? ").lower()
    mouth=input("Mouth shape? ").lower()
    style=input("Hair style? ").lower()
    nose=input("Nose style? ").lower()
    tache=input("Moustache style? ").lower()
    response = openai.Image.create(
    prompt=
    f"a face with {eye} eyes. big {hair}, {style} hair. a {mouth} mouth shape. a {nose} nose with a {tache} moustache. drawn by a programmer learning python (as if with the turtle module)",
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    response2 = requests.get(image_url, stream=True)
    with open('img.png', 'wb') as file:
        shutil.copyfileobj(response2.raw, file)
    del response2
    img = Image.open("img.png")
    img = img.convert("P")
    img.save("img.gif")

    win = turtle.Screen()
    win.bgpic('img.gif')
else:
    print("This is in progress!")