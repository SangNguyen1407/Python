def split(string:str, separator: str=" ") -> list:
    split_words = []
    last_index = 0
    for index, char in enumerate(string):
        if char == separator:
            split_words.append(string[last_index:index])
            last_index = index + 1
        elif index == len(string)-1:
            split_words.append(string[last_index:len(string)])
    return split_words

"""
if __name__ == "__main__":
    s = split("apple#banana#cherry#orange","#")
    print(s)
    s = split("12:43:39:89",":")
    print(s)
    s = split("apple,banana,cherry,orange",",")
    print(s)
"""