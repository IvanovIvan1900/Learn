#https://pythonist.ru/slots-v-python/
from pympler import asizeof
from datetime import datetime as dt

class Article:
    def __init__(self, date, writer):
        self.date = date
        self.writer = writer

class ArticleWithSlots:
    __slots__ = ["date", "writer"]
    
    def __init__(self, date, writer):
        self.date = date
        self.writer = writer
        
def test_size():
    article = Article("2020-01-01", "xiaoxu")
    article_slots = ArticleWithSlots("2020-01-01", "xiaoxu")
    print(asizeof.asizeof(article))
    print(asizeof.asizeof(article_slots))    

def Time(func):
    def wrapper(*args, **kwargs):
        time_start = dt.now()
        func(*args, **kwargs)
        time_stop = dt.now()
        print("Func {} work {:.5f} sec".format(func.__name__, (time_stop-time_start).total_seconds()))
    return wrapper    

@Time
def create_object(cls, size):
    for _ in range(size):
        article = cls("2020-01-01", "xiaoxu")

@Time
def access_attribute(obj, size):
    for _ in range(size):
        writer = obj.writer
    
def test_time():
    article = Article("2020-01-01", "xiaoxu")
    article_slots = ArticleWithSlots("2020-01-01", "xiaoxu")        
    print("Test acces atribute article/article_slots")    
    access_attribute(article, 1000000)
    access_attribute(article_slots, 1000000)
    
    print("Test create article/article_slots")    
    create_object(Article, 1000000)
    create_object(ArticleWithSlots, 1000000)
    
if __name__ == '__main__':
    test_size()
    test_time()