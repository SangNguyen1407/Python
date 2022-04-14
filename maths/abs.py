"""Absolute Value."""


def abs_val(num: int) -> int:
    if num < 0:
        num = -num
    return num

def abs_val1(num: int) -> int:
    return -num if num < 0 else num

if __name__ == "__main__":
    print(abs_val(-34))  # --> 34
    print(abs_val1(-34))