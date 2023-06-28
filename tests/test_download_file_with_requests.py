import os.path
import requests
from path import dir_tmp


# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь
def test_save_file_from_req():
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    path = os.path.join(dir_tmp, 'selenium_logo.png')
    response = requests.get(url)
    with open(path, 'wb') as file:
        file.write(response.content)
    size = os.path.getsize(path)
    assert size == 30803
    os.remove(path)
