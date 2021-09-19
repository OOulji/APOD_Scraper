import requests
from PIL import Image
from bs4 import BeautifulSoup
from datetime import date


def get_date():
    d=date.today().strftime("%y%m%d")
    return d

def main(date):
    data = requests.get("https://apod.nasa.gov/apod/ap"+date+".html")
    soup = BeautifulSoup(data.text, 'html.parser')

  
    image = soup.find('img')
    image_url = image['src']


    img = Image.open(requests.get("https://apod.nasa.gov/apod/"+image_url, stream = True).raw)
    img.save(date+".jpg")
    img.show()
    

if __name__ == "__main__":
    day = get_date()
    main(day)