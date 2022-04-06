from __future__ import annotations

def quick_sort (list_number: list) -> list:
    if len(list_number) < 2:
        return list_number
    pivot = list_number.pop()
    greater: list[int] = []
    lesser: list[int] = []
    for element in list_number:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    # [3,5,1,0,9,2]
    user_input = input("Enter numbers: ").strip()
    # create list numbers
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted))