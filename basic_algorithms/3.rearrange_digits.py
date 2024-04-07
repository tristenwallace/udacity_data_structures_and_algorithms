def merge_sort(input_list):
    if len(input_list) > 1:
        mid = len(input_list) // 2
        left_half = input_list[:mid]
        right_half = input_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                input_list[k] = left_half[i]
                i += 1
            else:
                input_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            input_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            input_list[k] = right_half[j]
            j += 1
            k += 1

def rearrange_digits(input_list):
    merge_sort(input_list)
    number1 = number2 = 0

    for i, value in enumerate(input_list):
        if i % 2 == 0:
            number1 = number1 * 10 + value
        else:
            number2 = number2 * 10 + value

    return [number1, number2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])