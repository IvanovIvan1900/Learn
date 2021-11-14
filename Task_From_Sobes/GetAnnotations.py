
def get_annotation(val: str):
    sp_val = val.split('=')[0]
    true_list = ['str' in sp_val, 'int' in sp_val, 'float' in sp_val]
    return (['str', 'int', 'float'][true_list.index(True)] if any(true_list) else None)

# мое
# def get_annotation(input_string: str):
#     annotation = None
#     array_param = input_string.split("=")
#     if len(array_param) > 0:
#         array_part= array_param[0].split(":")
#         if len(array_part) > 1:
#             annotation = array_part[1].strip()
#     return annotation

if __name__ == '__main__':
    assert get_annotation("a: str = 'b: int = 1'") == 'str'
    assert get_annotation('a: int') == 'int'
    assert get_annotation("a = 'b: int = 1'") is None
    assert get_annotation('a = 1') is None
    assert get_annotation('a=1') is None
    assert get_annotation('') is None