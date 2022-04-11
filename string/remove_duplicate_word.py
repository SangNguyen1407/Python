def remove_duplicates_word(sentence: str) -> str:
    return " ".join(set(sentence.split()))

if __name__ == "__main__":
    print(remove_duplicates_word("Python is great and Java is also great"))