from task_library import *


list_of_data = []
list_of_data.append({'param_input':{'str_in':'file'}, 'return_value':''})
list_of_data.append({'param_input':{'str_in':'.not_ext.'}, 'return_value':''})
list_of_data.append({'param_input':{'str_in':'.not_ext'}, 'return_value':''})
list_of_data.append({'param_input':{'str_in':'file.py.exe'}, 'return_value':'exe'})
list_of_data.append({'param_input':{'str_in':'script.py'}, 'return_value':'py'})



@check_function(data_check=list_of_data)
def get_ext_my(str_in: str)-> str:
    part_of_filenam = str_in.split('.')
    count_not_empty = 0
    for elem in part_of_filenam:
        if elem:
            count_not_empty += 1
            if count_not_empty > 1:
                break
    if count_not_empty > 1:
        return part_of_filenam[len(part_of_filenam)-1]
    else:
        return ''

@check_function(data_check=list_of_data)
def get_ext_solution(str_in: str) -> str:
    str_in = str_in.strip()
    separator = "."

    if str_in[0] == separator:
        return ''
    
    parts = str_in.split(separator)
    return parts[-1].strip() if len(parts) > 1 else ''

if __name__ == "__main__":
    get_ext_my('')
    get_ext_solution('')