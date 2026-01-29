
the_tuple = (1, 2, 3, 4, 5)

the_list = [1, 2, 3, 4, 5]
the_list[0] = 6



ltr: dict = {'a': 1, 'b': 2, 'c': 3}



letters: dict = {}
phrase: str = " The quick brown fox jumps over the lazy dog. "
for char in letters:
    if letters.get(char) is None:
        letters[char] = 1
        
    else:
        letters[char] += 1

for key, value in ltr.items():
    print(key, value)

class Cat():
    def __init__(self, name: str, color: str, age: int):
        self.name = name
        self.color = color
        self.age = age
    def say_age(self):
        print(self.age)

my_cat = Cat(1, 'cat', 'dog')
my_cat.say_age()