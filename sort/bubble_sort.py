def bubble_sort(list_numbers):
    length = len(list_numbers)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if list_numbers[j] > list_numbers[j + 1]:
                list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]

    return list_numbers

if __name__ == "__main__":
    # [3,5,1,0,9,2]
    user_input = input("Enter numbers: ").strip()
    # create list numbers
    unsorted = [int(item) for item in user_input.split(",")]
    print(bubble_sort(unsorted))