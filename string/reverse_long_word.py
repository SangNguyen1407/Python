def reverse_long_word(sentence: str) -> str:
    return " ".join("".join(word[::-1]) if len(word) > 4 else word for word in sentence.split())


if __name__ == "__main__":
    print (reverse_long_word("Hey wollef sroirraw"))
    print (reverse_long_word("nohtyP is nohtyP"))
    print (reverse_long_word("1 12 123 1234 54321 654321"))