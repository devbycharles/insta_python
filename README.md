# Instagram Bot for Posting Inspirational Quotes

This project is a Python-based Instagram bot that automates the process of posting inspirational quotes on your Instagram account. The bot pulls random images and inspirational quotes from the API Ninjas platform and overlays the quotes onto the images before posting them to your Instagram feed.

## Features

- Fetches random images from API Ninjas.
- Retrieves inspirational quotes from API Ninjas.
- Overlays the quotes onto the images.
- Posts the edited images with quotes to your Instagram feed.
- Supports dynamic resizing and centering of text to fit images of various dimensions.
- Ensures the text is wrapped properly to avoid cutting off quotes.
- Adds a black outline to ensure readability of the white text on various image backgrounds.

## Requirements

- Python 3.x
- instagrapi library
- PIL (Python Imaging Library) library

## How to Use

1. Clone the repository: `git clone https://github.com/yourusername/instagram-bot.git`
2. Install required libraries: `pip install instagrapi Pillow`
3. Replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your Instagram credentials in the `insta_bot.py` script.
4. Run the script: `python insta_bot.py`

The bot will log in to your Instagram account, fetch random images and inspirational quotes, overlay the quotes on the images, post them to your Instagram feed, and then log out.

**Note:** Be cautious while using automation bots to ensure compliance with Instagram's terms of use.

## Customization

- You can adjust the font size, outline size, and other parameters in the `insta_bot.py` script to match your preferences.
- Modify the `width` and `height` variables for API Ninjas requests to fetch images of desired dimensions.
- Change the width in the `TextWrapper` object to adjust text wrapping.

## Disclaimer

This project is for educational purposes and personal use only. Use it responsibly and in compliance with Instagram's terms of use.

## Credits

- This project uses the `instagrapi` library for interacting with Instagram.
- API Ninjas (https://api.api-ninjas.com/) provides random images and quotes for this bot.

