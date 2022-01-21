
def int_to_ip_my(int_in: int) -> str:
    str_hex = format(int_in, "X")
    array = [str(int(str_hex[x-2:x], base = 16)) for x in range(len(str_hex), 0, -2)]
    while len(array) < 4:
        array.append("0")
    
    return ".".join(reversed(array))

def int_to_ip_my_wich_bits(int_in: int)-> str:
    
    return ".".join([str((int_in >> num &0xFF)) for num in [24, 16, 8, 0]])
    
def int_to_ip_solution(num):
    pass

if __name__ == "__main__":
    # print(int_to_ip_my_wich_bits(2149583361))
    assert int_to_ip_my_wich_bits(32) == '0.0.0.32'
    assert int_to_ip_my_wich_bits(0) == '0.0.0.0'
    assert int_to_ip_my_wich_bits(2149583361) == '128.32.10.1'