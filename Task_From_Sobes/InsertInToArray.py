import timeit
import random

func  = None
array_input_data = None

def insert_into_my(input_array: list, input_value: int) -> int:
    index_from = 0
    index_to = len(input_array)-1
    index_rez = -1
    calculate = True
    while(calculate):
        if (index_to - index_from) < 4:
            for i in range(index_to - index_from+1):
                if input_array[index_from + i] == input_value or input_array[index_from + i] > input_value:
                    index_rez = index_from + i
                    calculate = False
                    break
            if calculate:
                raise Exception("Error in algoritm")
        else:
            median = index_from+(index_to - index_from)//2
            if input_array[median] > input_value:
                index_to = median
            else:
                index_from = median

    return index_rez

def insert_into_sloutions(input_array: list, input_value: int) -> int:
    for i, value in enumerate(input_array):
        if value >= input_value:
            return i


def test_function_on_data(func):
    # time_start = timeit.default_timer()
    global array_input_data
    for elem in array_input_data:
        assert func(elem[0], elem[1])  == elem[2]
    # assert func([1, 2, 4, 5], 4) == 2
    # assert func([1, 2, 3, 6], -1) == 0
    # time_run = (timeit.default_timer() - time_start)
    # print('Func is "{}" time is {:f}"'.format(func.__name__, time_run))

def calculate_function(func_in):
    count = 1
    global func
    func = func_in
    time = timeit.timeit(stmt="test_function_on_data(func)",globals=globals(),  number  = count)
    print("Functin is {}. Count run {}. Time work is {:8f}".format(func.__name__, count,  time))

def get_test_data():
    len_array = 1000000
    global array_input_data
    array_input_data = []
    print("calculate test data")
    for i in range(10):
        array = sorted([random.randint(0, 10000000) for i in range(len_array)])
        input_value = random.randint(0, 10000000)
        etalon_value = insert_into_sloutions(array, input_value)
        array_input_data.append((array, input_value, etalon_value))


if __name__ == '__main__':
    get_test_data()
    print("start test")
    calculate_function(insert_into_my)
    calculate_function(insert_into_sloutions)
