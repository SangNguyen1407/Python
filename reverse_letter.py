#    reverse_letters("I   love       Python")
#    'I evol nohtyP'

def reverse_letter(string:str, separator: str=" ") -> list:
    reverse = ""
    for letter in string.split(separator):
        reverse +=  letter[::-1]
        reverse += " "
    return reverse

def reverse_letter1(string:str, separator: str=" ") -> list:
    return "".join(letter[::-1] for letter in string.split(separator))


if __name__ == "__main__":
    print (reverse_letter("string", " "))
    print (reverse_letter("", " "))
    print (reverse_letter("string test reverse", " "))