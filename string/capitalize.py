"""
    This function will capitalize the first letter of a sentence or a word
    >>> capitalize("hello world")
    'Hello World'
    >>> capitalize("123 hello world")
    '123 Hello world'
    >>> capitalize(" hello world")
    ' Hello World'
    >>> capitalize("a")
    'A'
    >>> capitalize("")
    ''
    >>> capitalize("hello world 123 Hello test")
    'Hello World 123 Hello Test'
"""


def capitalize(sentence: str) -> str:
    if not sentence:
        return ""
    sentence = sentence.strip(" ")
    lower_to_upper = ""
    list_word = split.split(sentence, " ")
    for word in list_word:
        if "a" <= word[0] <="z":
            word = chr(ord(word[0])-32) + word[1:]
        lower_to_upper += word + " "
    return lower_to_upper.strip(" ")


def capitalize1(sentence: str) -> str:
    if not sentence:
        return ""
    sentence = sentence.strip(" ")
    list_word = split.split(sentence, " ")
    return " ".join(chr(ord(word[0])-32) + word[1:] if "a" <= word[0] <="z" else word for word in split.split(sentence, " "))

if __name__ == "__main__":
    import split
    print(capitalize("I am a sentence"))
    print(capitalize1("I am a sentence a a a "))
    print(capitalize("  "))
    print(capitalize("  A A."))
