import re

def to_camel_my(input:str) -> str:
    test = re.split('[-_]', input)
    return ''.join(s_part if idx == 0 else s_part.capitalize() for idx, s_part in enumerate(test))
    
def to_came_solution(string):
    map = str.maketrans('', '', "-_")    
    
    return string[0]+string.title().translate(map)[1:]
    
    
if __name__ == '__main__':
    assert to_came_solution('python_community_ru') == 'pythonCommunityRu'
    assert to_came_solution('Python-community-Ru') == 'PythonCommunityRu'