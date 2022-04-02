#    >>> reverse_words("I     Love          Python")
#    'Python Love I'
def reverse_words(input_str: str, separator: str=" ") -> str:   
    return " ".join(input_str.split(separator)[::-1])

if __name__ == "__main__":
    print (reverse_words("string test", " "))