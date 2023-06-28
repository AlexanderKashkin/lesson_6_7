import os
import zipfile
from zipfile import ZipFile
from path import dir_tmp, dir_main


def test_create_and_read_zip():
    files_res = os.listdir(dir_main)
    name_archive = 'test.zip'
    assert len(files_res) == 4, 'files in dir not is 4'
    path_for_zip = os.path.join(dir_tmp, name_archive)
    with zipfile.ZipFile(path_for_zip, mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zip_file_write:
        for file in files_res:
            zip_file_write.write(os.path.join(dir_main, file))
    assert os.path.exists(path_for_zip)
    assert os.path.isfile(path_for_zip)
    assert os.path.getsize(path_for_zip) == 1637685
    dict_files = {}
    with ZipFile(path_for_zip) as zip_file_read:
        for item in zip_file_read.infolist():
            dict_files.update({item.filename: item.file_size})
    assert len(dict_files) == 4
    path_in_zip = 'Users/Alexander/PycharmProjects/lesson_6_7/resources/'
    for k, v in dict_files.items():
        if k == f'{path_in_zip} + docs-pytest-org-en-latest.pdf':
            assert v == 1739253
        elif k == f'{path_in_zip} + file_example_XLSX_50.xlsx':
            assert v == 7360
        elif k == f'{path_in_zip} + hello.zip':
            assert v == 128
        elif k == f'{path_in_zip} + username.csv':
            assert v == 183
    os.remove(path_for_zip)
