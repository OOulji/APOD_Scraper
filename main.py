import requests
from PIL import Image
from bs4 import BeautifulSoup
from datetime import date


def get_date():
    d=date.today().strftime("%y%m%d")
    return d

def main(date):

    print("Connecting...\n")

    data = requests.get("https://apod.nasa.gov/apod/ap"+date+".html")

    print("Data request succesfull...\n")

    soup = BeautifulSoup(data.text, 'html.parser')

    image = soup.find('img')
    title = soup.find('title')

    if image is not None:
        image_url = image['src']
        img = Image.open(requests.get("https://apod.nasa.gov/apod/"+image_url, stream = True).raw)
        img.save("images/"+date+".jpg")
        print("Image found and saved!\n")
        print(title.get_text())
        img.show()
    else:
        print("No image found.")


if __name__ == "__main__":
    day = get_date()
    main(day)