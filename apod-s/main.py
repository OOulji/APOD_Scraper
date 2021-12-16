import requests
import argparse
import json
from PIL import Image
from bs4 import BeautifulSoup
from datetime import date


def get_date() -> str:
    current_date = date.today().strftime("%y%m%d")
    return current_date

def fetch_image(date: str, save_image: bool):

    print("Connecting...\n")

    data = requests.get("https://apod.nasa.gov/apod/ap"+date+".html")

    if data.status_code == 404:
        print("Today's image is not up yet!")
        return

    print("Data request succesfull...\n")

    soup = BeautifulSoup(data.text, 'html.parser')

    image = soup.find('img')
    title = soup.find('title')

    if image is not None:
        image_url = image['src']
        img = Image.open(requests.get("https://apod.nasa.gov/apod/"+image_url, stream = True).raw)
        if save_image : img.save(f'{date}.jpeg',"JPEG")
        print("Image found and saved!\n")
        print(title.get_text())
        img.show()
    else:
        print("No image found.")

def main():

    save_image = False

    parser = argparse.ArgumentParser(prog="apod-s",
                                    description="Retrieves NASA's Astronomy Picture of the day")
    
    parser.add_argument('-s','--save', action="store_true")

    args = parser.parse_args()

    if args.save:
        save_image = True

    date = get_date()
    fetch_image(date, save_image)



if __name__ == "__main__":
    main()