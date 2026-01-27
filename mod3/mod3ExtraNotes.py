
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