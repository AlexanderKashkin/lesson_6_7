import os.path
import time
from selenium import webdriver
from selene import browser

from path import dir_tmp


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp
def test_save_file_from_browser():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": dir_tmp,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)
    files_in_tmp = os.listdir(dir_tmp)
    assert len(files_in_tmp) == 1
    path_for_file = os.path.join(dir_tmp, files_in_tmp[0])
    os.path.exists(path_for_file)
    os.path.isfile(path_for_file)
    assert os.path.getsize(path_for_file) == 1578948

    os.remove(path_for_file)

