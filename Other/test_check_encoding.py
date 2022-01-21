import chardet
import urllib.request
import pytest
import tempfile
import os

# https://chardet.readthedocs.io/en/latest/usage.html


def test_request():
    rawdata = urllib.request.urlopen('http://yahoo.co.jp/').read()
    assert chardet.detect(rawdata) == {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}


test_data = [('Тестовая строка', 'utf-8'), 
    ('Тестовая строка', 'windows-1251'),
    ('Не поддерживаемая кодировка', 'cp866')
    ]
ids_test_data = [f'{t[0]} - {t[1]}'  for t in test_data]

@pytest.mark.parametrize('input_text, encoding_in',test_data, ids=ids_test_data)
def test_files(input_text, encoding_in):
    # input_text = 'test_string'
    # encoding = 'utf-8'
    tmp_dir = tempfile.gettempdir()
    file_name = os.path.join(tmp_dir, 'dav_test_encoding.txt')
    if os.path.isfile(file_name):
        os.remove(file_name)

    with open(file_name, 'w', encoding=encoding_in) as fp:
        fp.write(input_text)

    output_text = ''
    with open(file_name, 'rb') as fp:
        read_data = fp.read()
        char_encode_data = chardet.detect(read_data)
        output_text = read_data.decode(char_encode_data.get('encoding'))

    assert input_text == output_text