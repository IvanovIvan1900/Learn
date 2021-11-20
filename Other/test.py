
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
    print(test_try())