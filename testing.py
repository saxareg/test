some_list = [1, 2, 3, 1, 'hello', 3, 'hello']

# opition 1


def make_original(lst):
    original_list = []
    for item in lst:
        if item in original_list:
            continue
        original_list.append(item)
    return original_list


def other_make_original(lst):
    original_list = []
    for item in lst:
        if item not in original_list:
            original_list.append(item)
    return original_list


print(make_original(some_list))
