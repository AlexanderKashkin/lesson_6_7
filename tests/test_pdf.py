import os.path
from pypdf import PdfReader
from path import dir_main


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_pdf():
    my_pdf = os.path.join(dir_main, 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(my_pdf)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(f'{page=}')
    assert page['/Type'] == '/Page', 'for key /type value is not /page'
    assert number_of_pages == 412, 'numbers of page is not 412'
    assert text == 'pytest Documentation\nRelease 0.1\nholger krekel, trainer and consultant, https://merlinux.eu/\nJul 14, 2022', 'test is not included pytest Documentation..'
    assert os.path.getsize(my_pdf) == 1739253, 'size is not 1739253'
