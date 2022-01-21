import colorsys

def convert_to_rgb_my(h:float, l:float, s:float) :
    tuple_output = colorsys.hls_to_rgb(h,l, s)
    return (round(tuple_output[0], 2), round(tuple_output[1], 2), round(tuple_output[2], 2))
    
if __name__ == '__main__':
    assert convert_to_rgb_my(1, 1, 1) == (1, 1.0, 1.0)
    assert convert_to_rgb_my(0.9, 0.5, 0.5) == (0.75, 0.25, 0.55)
    assert convert_to_rgb_my(0.72, 0.624, 0.48) == (0.56, 0.44, 0.8)