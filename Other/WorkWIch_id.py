# Какие объекты зависят от реализации Python? В CPython 3.7 интернированными являются:

    # Целые числа в диапазоне от -5 до 256.
    # Строки, содержащие только ASCII-буквы, цифры или знаки подчёркивания.


    # Так сделано потому, что эти переменные очень часто используются во многих программах. Интернируя, Python предотвращает выделение памяти для постоянно используемых объектов.

    # Строки размером меньше 20 символов и содержащие ASCII-буквы, цифры или знаки подчёркивания будут интернированы, поскольку предполагается, что они будут применяться в качестве идентификаторов:
# https://habr.com/ru/company/vk/blog/454324/

# is - сравнивает, что ссылки указывают на один и тот же объект, т.к. None - это синглтон, то
# его надо сравнивать через is

# https://pythobyte.com/guide-to-string-interning-in-python-8499dba3/
# Вплоть до версии 3.7 Python использовал оптимизацию peephole, и все строки длиной более 20 символов не интернировались. Однако теперь он использует оптимизатор AST , и (большинство) строк до 4096 символов интернируются.
# Строки доступны только во время компиляции, это означает, что они не будут интернированы, если их значение не может быть вычислено во время компиляции.
def test_id():
    class Test():
        pass
    test_string_one = "hello"
    test_string_two = "hello"
    
    test_sring_one_not = 'foobar qwertyuiop!@#%^'
    test_sring_two_not = 'foobar qwertyuiop!@#%^'
    
    test_int_one = 125
    test_int_two = 125

    test_int_one_not = 1000
    test_int_two_not= 700+300
    
    class_one = Test()
    class_two = Test()
    
    print(id(test_string_one) == id(test_string_two))
    print(id(test_sring_one_not) == id(test_sring_two_not))
    print(id(test_int_one) == id(test_int_two))
    print(id(test_int_one_not) == id(test_int_two_not))
    print(id(class_one) == id(class_two))
    
    
if __name__ == '__main__':
    test_id()
    
