sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print(sample_dict)

def key_exists(dictionary, key):
    return key in dictionary

sample_dict = {0: 10, 1: 20}
key_to_check = 1
print(key_exists(sample_dict, key_to_check))

sample_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in sample_dict.items():
    print(key, value)

square_dict = {i: i ** 2 for i in range(1, 16)}
print(square_dict)

sample_string = 'marolix technology'
letter_count = {}

for letter in sample_string:
    letter_count[letter] = letter_count.get(letter, 0) + 1

print(letter_count)

sample_dict = {'a': 10, 'b': 20, 'c': 30}
total_sum = sum(sample_dict.values())
print(total_sum)


from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = Counter(d1) + Counter(d2)
print(combined_dict)

sample_dict = {0: 'physics', 1: 'math', 2: 'chemistry'}
key_index = 1
key_at_index = list(sample_dict.keys())[key_index]
print(sample_dict[key_at_index])

sample_dict = {'a': 10, 'b': 20, 'c': 30}
key_to_remove = 'b'
if key_to_remove in sample_dict:
    del sample_dict[key_to_remove]
print(sample_dict)

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

merged_dict = {**d1, **d2}
print(merged_dict)

