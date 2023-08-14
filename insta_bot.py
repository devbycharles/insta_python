from instagrapi import Client
from PIL import Image, ImageDraw, ImageFont
from textwrap import TextWrapper
import random
import os
import requests
import shutil
import time

# Log in to Instagram
cl = Client()
cl.login("INSERT USERNAME HERE", "INSERT PASSWORD HERE")

# API Ninjas Configuration
api_key = "INSERT API KEY HERE"
width = '1080'
height = '1080'
category = 'nature'
category_quote = 'inspirational'
api_url = f"https://api.api-ninjas.com/v1/randomimage?category={category}&width={width}&height={height}"
api_url_quote = f'https://api.api-ninjas.com/v1/quotes?category={category_quote}'

# Fetch Random Image URL from API Ninjas
response = requests.get(api_url, headers={'X-Api-Key': api_key, 'Accept': 'image/jpg'}, stream=True)
if response.status_code == requests.codes.ok:
    with open('img.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
else:
    print("Error:", response.status_code, response.text)
    exit()

# Fetch Random Inspirational Quote from API Ninjas
response = requests.get(api_url_quote, headers={'X-Api-Key': api_key})
if response.status_code == requests.codes.ok:
    quote_data = response.json()
    if isinstance(quote_data, list) and len(quote_data) > 0:
        random_quote = random.choice(quote_data)
        quote = random_quote.get("quote", "")
    else:
        print("No quotes found in the API response.")
        quote = ""
else:
    print("Error:", response.status_code, response.text)

# Overlay Quote on Image
img = Image.open("img.jpg")
draw = ImageDraw.Draw(img)
font_size = 36
font = ImageFont.truetype("Geneva.ttf", font_size)

# Create a TextWrapper object for wrapping the text
text_wrapper = TextWrapper(width=40)

# Wrap the quote text
wrapped_text = text_wrapper.fill(quote)

# Calculate x and y positions for centering the text
x = img.width // 4
y = img.height // 2

# Draw the black outline around the text
outline_color = "black"
outline_size = 2
draw.multiline_text((x - outline_size, y - outline_size), wrapped_text, font=font, fill=outline_color)
draw.multiline_text((x + outline_size, y - outline_size), wrapped_text, font=font, fill=outline_color)
draw.multiline_text((x - outline_size, y + outline_size), wrapped_text, font=font, fill=outline_color)
draw.multiline_text((x + outline_size, y + outline_size), wrapped_text, font=font, fill=outline_color)

# Draw the white text on top
draw.multiline_text((x, y), wrapped_text, fill="white", font=font)

# Save the Image with Overlay
img.save("img_with_quote.jpg")

# Clean up temporary image file function
def CleanUp():
    try:
        os.remove("img.jpg")
        os.remove("img_with_quote.jpg")
    except:
        pass

# Function to upload image, make a caption, then sign out of Instagram
def RunScript():
    caption = f'{quote} \n \n \n #quotes #motivation #mindfulness #mindset #positivevibes'
    try:
        cl.photo_upload("img_with_quote.jpg", caption=caption)
    except Exception as e:
        print("Error uploading image to Instagram:", e)
    finally:
        print('Posted')
        print('Sleeping...')

        CleanUp()
        cl.logout()
        time.sleep(3)

# Runs the Python script
RunScript()