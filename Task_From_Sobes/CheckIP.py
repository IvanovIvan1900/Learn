
def check_ip_my(input: str) -> bool:
    array_split = input.split('.')
    array_top = [255, 255, 255, 254]
    array_bottom = [1, 0, 0, 1]
    array_check = [bottom <= int(x) <= top for bottom, x, top in zip(array_bottom,
                                                                array_split, array_top) ]

    return len(array_check) == 4 and all(array_check)

if __name__ == '__main__':
    assert check_ip_my('10.10.10.10')
    assert check_ip_my('255.255.255.254')
    assert not check_ip_my('192.168.0.0')
    assert check_ip_my('192.168.0.1')
    assert not check_ip_my('192.168.0.255')