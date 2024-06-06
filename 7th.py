my_dict = {'b': 3, 'a': 1, 'c': 2}

sorted_dict_by_keys = dict(sorted(my_dict.items(), key=lambda x: x[0]))

print(sorted_dict_by_keys)
