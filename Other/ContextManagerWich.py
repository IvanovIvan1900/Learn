# https://docs.python-guide.org/writing/structure/ search Context Managers


# context manager from class
class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

def test_CM_object(fileName:str):
    with CustomOpen(fileName) as f:
        contents = f.read()
        print(contents)

# context manager from iterator
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

def test_CM_iterator(fileName:str):
    with custom_open(fileName) as f:
        contents = f.read()
        print(contents)
    

# test

if __name__ == '__main__':
    test_CM_object("")   