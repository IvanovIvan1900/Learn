from operator import itemgetter, attrgetter, methodcaller


def sort_grades_my_two(array_input: list)-> list:
    dic_of_key = {'F':1, 'C':2, 'B':3, 'A':4}
    tuple_input = [(item.upper(), dic_of_key[item.upper()]) for item in array_input]
    
    return [item[0] for item in sorted(tuple_input, key=itemgetter(1))]

def sort_grades_my(array_input: list)-> list:
    array_upper = [item.upper() for item in array_input]
    return sorted(array_upper, reverse= True)


def sort_grade_solution(array_input: list) -> list:
    dic_of_key = {'F':1, 'C':2, 'B':3, 'A':4}

    return sorted((i.upper() for i in array_input) , key=lambda x: dic_of_key[x])

def test_function(f):
    assert f(['A', 'B', 'C', 'C', 'F', 'A']) == ['F', 'C', 'C', 'B', 'A', 'A']
    assert f(['b', 'c', 'C', 'f', 'A']) == ['F', 'C', 'C', 'B', 'A']
    assert f([]) == []    
    print(f'Function {f.__name__} is ok')
    
if __name__ == '__main__':
    test_function(sort_grades_my)
    test_function(sort_grades_my_two)
    test_function(sort_grade_solution)