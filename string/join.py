"""
Program to join a list of strings with a given separator
"""

def join(separator: str, separated: list) -> str:
    string = ""
    for word_phrase in separated:
        string += word_phrase + separator
    return string.strip(separator)

if __name__ == "__main__":
    print(join("#", ["You", "are", "amazing!"]))