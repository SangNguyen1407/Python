def is_palindrome_reverse_string(s: str) -> bool:
    return s == s[::-1]

def is_palindrome(s: str) -> bool:
    start_i = 0
    end_i = len(s) - 1
    while start_i < end_i:
        if s[start_i] == s[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False       
    return True


if __name__ == "__main__":
    print("palidrome")
    print (is_palindrome("amanaplanacanalpanama"))
    print (is_palindrome_reverse_string("amanaplanacanalpanama"))