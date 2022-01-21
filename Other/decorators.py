from pprint import pprint
# https://tproger.ru/translations/demystifying-decorators-in-python/

#==========================================================
def easy_decorator(func):
    def wrapper():
        print("Декоратор для функции без параметров. ДО")
        func()
        print("Декоратор для функции без параметров. После")
    return wrapper

@easy_decorator
def easy_function():
    print("Выполнение функции")


#==========================================================
def decorator_wich_func_param(func):
    import time
    
    def wrapper(*args, **kwargs):
        print("Вызвали функцию {}".format(func.__name__,))
        print("*args")
        pprint(args)
        print("**kwargs")
        pprint(kwargs)
        return_value = func(*args, **kwargs)
        print("Результат функции {}".format(return_value))
        return return_value
    return wrapper

@decorator_wich_func_param
def eays_function_wich_param(test_param:str, test_value: str = None) -> str:
    print("run function")
    return "Возвращаемое значение"

#==========================================================

def deocorator_func_wich_param(iters):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Функция выполняется {iters} раз, этот параметр задается в декораторе')
            for i in range(iters):
                return_value = func(*args, **kwargs)
            return return_value

        return wrapper
    return actual_decorator


@deocorator_func_wich_param(iters = 5)
def eays_function_wich_param_decordunc(test_param:str, test_value: str = None) -> str:
    print("run function")
    return "Возвращаемое значение"


#==========================================================
# удобно использовать если надо сохранить какие-то параметры между вызовами функции
class DecoratorWichParamClass:
    def __init__(self, iters):
        print('> Класс Decorator метод __init__')
        self.iters = iters

    def __call__(self, func):
        def new_func(*args, **kwargs):
            print('> перед вызовом класса...', func.__name__)
            result_value = func(*args, **kwargs)
            print('> после вызова класса')
        
        return new_func
        
@DecoratorWichParamClass(iters = 5)
def eays_function_wich_param_decor_class(test_param:str, test_value: str = None) -> str:
    print("run function")
    return "Возвращаемое значение"


if __name__ == '__main__':
    easy_function()
    print("======================================================")
    res_value = eays_function_wich_param("value test param", test_value = "value test value")
    print("======================================================")
    res_value = eays_function_wich_param_decordunc("value test param", test_value = "value test value")
    print("======================================================")
    res_value = eays_function_wich_param_decor_class("value test param", test_value = "value test value")