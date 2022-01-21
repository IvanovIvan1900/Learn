from datetime import datetime as dt
# list_of_data = []
# list_of_data.append({'param_input':{'array_in':[1, 6, 3, 2]}, 'return_value':9})
# list_of_data.append({'param_input':{'array_in':[1, 2, 3]}, 'return_value':0})
# list_of_data.append({'param_input':{'array_in':[4, 5, 3, 2, 0]}, 'return_value':1})
# list_of_data.append({'param_input':{'array_in':}, 'return_value':})


# test_data = {"array_in": []}


def check_function(data_check):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            check_is_correct = True
            for elem in data_check:
                return_value = func(**elem.get("param_input", {}))
                if return_value != elem.get("return_value"):
                    check_is_correct = False
                    print(f'Funcition {func.__name__,} is not correct. Input data {str(elem.get("param_input", {}))}, output data etalon {elem.get("return_value")}, function get {return_value}')
            
            print(f'Function "{func.__name__: >30}" check is {"correct" if check_is_correct else "NOT CORRECT"}')
            
        return wrapper
    return actual_decorator
            
def test_speed(data_in, iter:int):
    """Test speed function

    Args:
        data_in ([type]): test data - dic of **kwargs
        iter (int): count start funcion
    """    
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = dt.now()
            for elem in range(iter):
                func(**data_in)
            stop_time = dt.now()
            time_in_sec = (stop_time - start_time).total_seconds()
            print(f'Function "{func.__name__: >30}" time work {time_in_sec}')
            
        return wrapper
    return actual_decorator
    