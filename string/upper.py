def upper(word: str) -> str:
    string = ""
    for char in word:
        if "a" <= char <="z":
            string += chr(ord(char)-32)
        else:
            string += char
    return string

def upper1(word: str) -> str:
    return "".join(chr(ord(char)-32) if "a" <= char <="z" else char for char in word )

if __name__ == "__main__":
    print(upper("woW"))
    print(upper("hellO"))
    print(upper("wh[]123"))
    print(upper1("wh[]123"))