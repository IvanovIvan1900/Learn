
def calculate_my(array_input: list)-> int:
    array_sort = sorted(array_input)
    array_correct = []
    index  = 1
    summ = 0
    array_correct.append(array_sort[0])
    half_len = (len(array_input)-1)//2 
    is_even = (len(array_input)-1)% 2 == 0
    while (index < half_len or (index == half_len and is_even)):
        array_correct.append(array_sort[-index])
        if index < half_len:
            array_correct.insert(0, array_sort[-(index+1)])
        array_correct.append(array_sort[index])
        if index < half_len:
            array_correct.insert(0, array_sort[index+1])
        index += 2
    if not is_even:
        array_correct.append(array_sort[index])
        
    for x in range(1, len(array_input)):
        summ += abs(array_correct[x-1]-array_correct[x])    
        
    
    return summ

def calculate_solution(data: list):
    s_list = sorted(data)

    s_list[0], s_list[1] = s_list[1], s_list[0]

    res = list(s_list.pop(0) if i % 2 == 0 else s_list.pop() 
    for i in range(len(s_list)))

    return sum(abs(x - y) for x, y in zip(res[:-1], res[1:]))

def check_result(func, result_etalon, *args):
    result_get = func(*args)
    if result_get !=  result_etalon:
        print("Error. etalon {}, get {}, input param {}, ".format(result_etalon, result_get, args))

if __name__ == '__main__':
    func = calculate_my
    # func = calculate_solution
    check_result(func, 22, [3, 1, 7, 5, 9])
    check_result(func, 41, [1, 6, 13, 9, 3, 2])
    check_result(func, 3, [2, 3, 4])
    
    print("Check is done")