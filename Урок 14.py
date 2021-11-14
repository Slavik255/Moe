# Функия скачивания изображений
import random
import urllib.request
names = []

def download_img(url):
    name = random.randrange(1, 100)
    name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, name)
#  Сдесь указываем ссылку на изображение
try:
    download_img("https://pythonru.com/wp-content/uploads/2021/01/zachem-nuzhno-uchit-python.png")
except:
    print("Нет выполнения")


