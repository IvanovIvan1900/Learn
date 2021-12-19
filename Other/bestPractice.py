# https://docs.python-guide.org/writing/style/

#+++++++++++++++++++++++++++++
#       unpacking
#+++++++++++++++++++++++++++++

a = 4
b = 6
c = 7

a, b = b, a

a, (b, c) = 1, (2, 3)

a, *rest = [1, 2, 3]
# a = 1, rest = [2, 3]
a, *middle, c = [1, 2, 3, 4]
# a = 1, middle = [2, 3], c = 4

#+++++++++++++++++++++++++++++
#       ignored variable
#+++++++++++++++++++++++++++++

filename = 'foobar.txt'
basename, __, ext = filename.rpartition('.')

#+++++++++++++++++++++++++++++
#       list
#+++++++++++++++++++++++++++++
four_nones = [None] * 4

letters = ['s', 'p', 'a', 'm']
word = ''.join(letters)

s = set(['s', 'p', 'a', 'm'])
l = ['s', 'p', 'a', 'm']

# значительно быстрее,т.к это хеш таблица
def lookup_set(s):
    return 's' in s

def lookup_list(l):
    return 's' in l

#+++++++++++++++++++++++++++++
#       dict
#+++++++++++++++++++++++++++++
# good
d = {'hello': 'world'}

print(d.get('hello', 'default_value')) # prints 'world'
print(d.get('thingy', 'default_value')) # prints 'default_value'

# Or:
if 'hello' in d:
    print(d['hello'])

# bad
# needlessly allocates a list of all (gpa, name) entires in memory
valedictorian = max([(student.gpa, student.name) for student in graduates])

# good
valedictorian = max((student.gpa, student.name) for student in graduates)

# good
def make_batches(items, batch_size):
    """
    >>> list(make_batches([1, 2, 3, 4, 5], batch_size=3))
    [[1, 2, 3], [4, 5]]
    """
    current_batch = []
    for item in items:
        current_batch.append(item)
        if len(current_batch) == batch_size:
            yield current_batch
            current_batch = []
    yield current_batch
    
    
# bad
[print(x) for x in sequence]

# good
for x in sequence:
    print(x)
    
# bad
# Filter elements greater than 4
a = [3, 4, 5]
for i in a:
    if i > 4:
        a.remove(i)

while i in a:
    a.remove(i)
    
# good
# comprehensions create a new list object
filtered_values = [value for value in sequence if value != x]

# generators don't create another list
filtered_values = (value for value in sequence if value != x)

# replace the contents of the original list
sequence[::] = [value for value in sequence if value != x]


# bad
# Add three to all list members.
a = [3, 4, 5]
b = a                     # a and b refer to the same list object

for i in range(len(a)):
    a[i] += 3             # b[i] also changes
    
# good
a = [3, 4, 5]
b = a

# assign the variable "a" to a new list without changing "b"
a = [i + 3 for i in a]

#+++++++++++++++++++++++++++++
#       string
#+++++++++++++++++++++++++++++

# bad
my_very_big_string = """For a long time I used to go to bed early. Sometimes, \
    when I had put out my candle, my eyes would close so quickly that I had not even \
    time to say “I’m going to sleep.”"""

from some.deep.module.inside.a.module import a_nice_function, another_nice_function, \
    yet_another_nice_function
    
# good
my_very_big_string = ("For a long time I used to go to bed early. Sometimes, \
    when I had put out my candle, my eyes would close so quickly that I had not even \
    time to say “I’m going to sleep.”")

from some.deep.module.inside.a.module import a_nice_function, another_nice_function, \
    yet_another_nice_function

def test_strange_boolean():
    # https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
    print('0 or 10 = {}'.format(0 or 10))
    print('1 or 10 = {}'.format(1 or 10))
    print('0 and 10 = {}'.format(0 and 10))
    print('1 and 10 = {}'.format(1 and 10))