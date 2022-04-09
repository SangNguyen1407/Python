"""
https://en.wikipedia.org/wiki/N-gram
"""
"""
Create ngrams from a sentence
>>> char_ngram("I am a sentence", 2)
['I ', ' a', 'am', 'm ', ' a', 'a ', ' s', 'se', 'en', 'nt', 'te', 'en', 'nc', 'ce']
>>> char_ngram("I am an NLPer", 2)
['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
>>> char_ngram("This is short", 50)
[]
"""

def char_ngram(sentence: str, ngram_size: int) -> list:
    ngram = []
    for i in range(len(sentence) - ngram_size + 1):
        ngram.append(sentence[i: i + ngram_size])
    return ngram

def char_ngram1(sentence: str, ngram_size: int) -> list:
    return [sentence[i : i + ngram_size] for i in range(len(sentence) - ngram_size + 1)]

def word_ngram(sentence: str, ngram_size: int) -> list:
    ngram = []
    list_word = split.split(sentence, " ")
    for i in range(len(list_word) - ngram_size + 1): 
        ngram.append(list_word[i : i + ngram_size])
    return ngram

def word_ngram1(sentence: str, ngram_size: int) -> list:
    list_word = split.split(sentence, " ")
    return [list_word[i : i + ngram_size] for i in range(len(list_word) - ngram_size + 1)]

if __name__ == "__main__":
    import split
    print(char_ngram("I am a sentence", 2))
    print(char_ngram1("I am a sentence", 2))
    print(word_ngram("I am a sentence", 2))
    print(word_ngram1("I am a sentence", 2))
    print(char_ngram("This is short", 50))