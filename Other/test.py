import datetime

# def test_id():
#     s = (1,1, 'a')
#     s2 = (1,1, 'a')
#     print(id(s) == id(s2))

# def test_try() -> int:
#     try:
#         return 0/0
#         print(1)
#     except:
#         print(2)
#         return 3
#     finally:
#         print(4)

def get_str(a:str, b:str) -> str:
    return a + b

def get_tup(a, b):
    return a+1, b-1
        
def test_get():
    s1 = get_str("hel", "lo")
    s2 = get_str("hel", "lo")
    
    t1 = get_tup(1, 2)
    t2 = get_tup(1, 2)
    
    print(id(s1) == id(s2))
    print(id(t1) == id(t2))
    

def convert_timedelat_to_human(timed):
    sec = timed.total_seconds()
    # days = seconds // 86400
    hours = sec // 3600 % 24
    minutes = sec // 60 % 60
    seconds = sec % 60    
    return f'{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}'
    

def test_class_var():
    a = ''
    t = type(a)
    t.a = "hello"
    print(str.a)
    
def test_unpack():
    dic_of_tuple = {"test_key":('value1', 'vaslue2')}
    for key, (value1, value2) in dic_of_tuple.items():
        print("succes")
    
    
def test_set():
    s = set('abc')
    s.add('def')
    s.update(['p', 'q'])
    
    print(sorted(s))
    
def test_num(num):
    return num-1 or num+1 and num*3
    
def test_strange_boolean():
    print('0 or 10 = {}'.format(0 or 10))
    print('1 or 10 = {}'.format(1 or 10))
    print('0 and 10 = {}'.format(0 and 10))
    print('1 and 10 = {}'.format(1 and 10))


if __name__ == '__main__':
    # print(convert_timedelat_to_human(datetime.timedelta(seconds=5*34*60)))
    #test_get()
    # test_unpack()
    #test_class_var()
    # test_set()
    #print(test_num(1))
    test_strange_boolean()