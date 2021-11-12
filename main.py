# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test_vklychenie():
    word = 'letters'
    letter_counts = {letter: word.count(letter) for letter in set(word)}
    print(letter_counts)

    list_chet = [number for number in range(1, 10) if number % 2 == 0]
    print(list_chet)


def test_unicode(test_value):
    """Процедура использует различные функции unicode"""
    import unicodedata
    # так и не нашел, как можно получить код символа, чтобы вставить в строку, только имя
    # symbol = '{'
    # print('unicode escate sym {{ is {}'.format(symbol.encode("unicode_escape")))
    print("++++++++++++++++TEST UNICODE+++++++++++++++++")
    unicodename = unicodedata.name(test_value)
    print('vaslue is "{}", unicode name is "{}" '.format(test_value, unicodename))

    unicode_sym_one = '\u00a2'  # Символ \u, за которым располагаются четыре шестнадцатеричных числа
    print('sym \\u00a2 is "{}"'.format(unicode_sym_one))

    # unicode_sym_two = '\U' #за которым следуют восемь шест-
    # надцатеричных символов, крайний слева из них должен быть равен 0

    unicode_sym_from_name = '\N{ASTERISK}'
    print('sym from name \\N{{ASTERISK}} is {}'.format(unicode_sym_from_name))
    # если мы заменяем с помощью unicode символов - то скобки надо так же дублировать
    print('sym from name \\N\u007B\u007BASTERISK\u007D\u007D is {}'.format(unicode_sym_from_name))


def test_format():
    """Тестируем работу в форматированием строки"""
    print("++++++++++++++++TEST FORMAT+++++++++++++++++")
    n = 10
    f = 115.2
    s = "test string"

    print("test fromat 1 {} {} {}".format(n, f, s))
    print("test fromat 2 {2} {1} {0}".format(n, f, s))

    print("test fromat 3 {n} {f} {s}".format(n=10, f=115.2, s="test string"))

    d = {'n': 10, 'f': 155.2, 's': "test string"}
    print("test format dic {0[n]} {0[f]} {0[s]} {1}".format(d, "other string"))

    # https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html
    print("test fromat  {0:5d} {1:^10f} {2:<20s}".format(n, f, s))
    print("test fromat  {0:!^20} ".format("BIG SALE"))


def test_byte():
    import struct  # служит для преобразования данныих из байтов в данные python
    blist = [1, 2, 3, 255]
    byte_immutable = bytes(blist)  # не изменяемый
    byte_array = bytearray(blist)  # изменяемый

    # возьмем массив - это начало файла png и извлечем из него ширину и высоту изображения
    valid_png_header = b'\x89PNG\r\n\x1a\n'
    data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
        b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
    if data[:8] == valid_png_header:
        widht, haight = struct.unpack(">LL", data[16:24])

    else:
        print("not valid data")

    test_number = 155
    byte_test_nubmer = struct.pack(">L", test_number)
    resutl_number = struct.unpack(">L", byte_test_nubmer)[0]
    print('Test number "{}", byte test number "{}", result test number "{}"'.format(test_number,
            byte_test_nubmer, resutl_number))

    # интересная штука, но я так и не разобрался как работает, пример из книшки не звлетел
    # byte_test_nubmer, resutl_number))
    # from construct import Struct, Int32ub, Const, String
    # # обработаем наши данные по картинке с помощью стороннего пакета
    # fmt = Struct('png',
    # Const(String('type', 8)),
    # Int32ub('length'),
    # Const(String('type', 4), b'IHDR'),
    # Int32ub('width'),
    # Int32ub('height')
    #              )
    # result = fmt.parse(data)
    # pprint(result)


def test_frimework_pase_page():
    import requests
    from bs4 import BeautifulSoup as soup
    url = "https://fishki.net/3993694-30-faktov-ot-kotoryh-murashki-begut-po-kozhe.html"
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    for child in doc.recursiveChildGenerator():
        if child.name:
            print(child.name)


def test_time():
    import time
    import pprint
    import locale
    from datetime import date

    epoch_time = time.time()
    print("epoch time {}".format(epoch_time))
    pprint.pprint("local time {}".format(time.localtime(epoch_time)))
    pprint.pprint("UTC time {}".format(time.gmtime(epoch_time)))

    # покажем работу с разными локалями
    names = locale.locale_alias.keys()
    # good_locale = [name for name in names if \
    #               name.startswith("ru") and len(name) == 5 ]
    good_locale = ['ru_RU', 'UTF-8']
    halloween = date(2014, 10, 31)
    for lang_country in good_locale:
        try:
            locale.setlocale(locale.LC_TIME, lang_country)
            halloween.strftime('%A, %B %d')
        except Exception as e:
            print("Error local {} is not correct".format(lang_country))



if __name__ == '__main__':
    z = 4
    # test_vklychenie()

    # test_unicode("S")
    # test_unicode("*")

    # test_format()

    # test_byte()

    # test_frimework_pase_page()

    # test_time()

