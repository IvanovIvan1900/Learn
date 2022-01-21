def hex_to_rgb_my(s_input: str): 
    return tuple(int(s_input[x:x+2], 16) for x in range (0, len(s_input), 2))

if __name__ == '__main__':
    assert hex_to_rgb_my('ffffff') == (255, 255, 255)
    assert hex_to_rgb_my('000000') == (0, 0, 0)
    assert hex_to_rgb_my('12A2B6') == (18, 162, 182)