"""
Prefix-function computation in Knuth-Morris-Pratt Algorithm
    >>> prefix_function("aabcdaabc")
    [0, 1, 0, 0, 0, 1, 2, 3, 4]
    >>> prefix_function("asdasdad")
    [0, 0, 0, 1, 2, 3, 4, 0]
"""
def prefix_function(input_string: str) -> list:
    # list the result values [0, 0, 0, ...len]
    prefix_result = [0] * len(input_string)

    for i in range(1, len(input_string)):
        j = prefix_result[i - 1] # [(i - j), i] is prefix-function

        while j > 0 and input_string[j] != input_string[i] :
            j = prefix_result[j - 1]
        
        if input_string[i] == input_string[j]:
            j += 1
        
        prefix_result[i] = j

    return prefix_result

def prefix_max(input_string: str) -> int:
    return max(prefix_function(input_string))

if __name__ == "__main__":
    print(prefix_max("aabcdaabc"))
    print(prefix_max("abcdefcde"))