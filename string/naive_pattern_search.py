def naive_pattern_search(s: str, pattern: str) -> list:
    position = []
    pat_len = len(pattern)
    for i in range(len(s) - pat_len + 1):
        match = True
        for j in range(pat_len):
            if s[i + j] != pattern[j]:
                match = False
                break

        if match:
            position.append(i)
            i += pat_len

    return position


if __name__ == "__main__":
    print(naive_pattern_search("ABAAABCDBBABCDDEBCABC", "ABC"))
    print(naive_pattern_search("ABCDEGFTEST", "TEST"))
    print(naive_pattern_search("TEST", "TEST"))
    print(naive_pattern_search("ABC", "ABAAABCDBBABCDDEBCABC"))