import csv
import os.path
from path import dir_main


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
#
def test_csv():
    name_file = 'eggs.csv'
    data = os.path.join(dir_main, name_file)

    # проверим наличие такого объекта и является ли он файлом, и если да, то удалим его
    if os.path.exists(data):
        if os.path.isfile(data):
            os.remove(data)

    with open(data, 'w', newline="") as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(data) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            assert len(row) == 3, 'len rows is not 3'
            assert isinstance(row, list), 'type is not list'
        assert os.path.getsize(data) == 34, 'size is not 34'

    os.remove(data)
