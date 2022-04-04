def lower(word: str) -> str:
    string = ""
    for char in word:
        if "A" <= char <= "Z":
            string += chr(ord(char) + 32)
        else:
            string += char
    return string

def lower1(word: str) -> str:
    return "".join(chr(ord(char) + 32) if "A" <= char <= "Z" else char for char in word )

if __name__ == "__main__":
    print(lower("woW"))
    print(lower("TEST[123]tEst"))
    print(lower1("TEST[123]tEst"))