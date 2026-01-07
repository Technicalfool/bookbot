def word_count(input_string):
    return len(input_string.split())


def char_stats(input_string):
    new_dict = {}
    for char in list(input_string):
        new_char = char.lower()
        if new_char in new_dict:
            new_dict[new_char] += 1
        else:
            new_dict[new_char] = 1
    return new_dict


def sort_on(items):
    return items["num"]


def char_stats_sorted(input_dict):
    new_list = []
    for key in input_dict:
        if key.isalpha():
            new_list.append({"char": key, "num": input_dict[key]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
