
def test_id():
    s = (1,1, 'a')
    s2 = (1,1, 'a')
    print(id(s) == id(s2))

def test_try() -> int:
    try:
        return 0/0
        print(1)
    except:
        print(2)
        return 3
    finally:
        print(4)
        
        
if __name__ == '__main__':
    test_id()