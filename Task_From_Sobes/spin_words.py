
from task_library import *

list_of_data = []
list_of_data.append({'param_input':{'input_str':'to'}, 'return_value':'to'})
list_of_data.append({'param_input':{'input_str':'Welcome'}, 'return_value':'emocleW'})
list_of_data.append({'param_input':{'input_str':'Hi everyone'}, 'return_value':'Hi enoyreve'})
list_of_data.append({'param_input':{'input_str':'This sentence is a sentence'}, 'return_value':'This ecnetnes is a ecnetnes'})

@check_function(data_check = list_of_data)
def spin_words_my(input_str: str) -> str:
    return " ".join(x if len(x) <5 else x[::-1] for x in input_str.split())

if __name__ == "__main__":
    spin_words_my([])