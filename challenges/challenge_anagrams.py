def merge(words, start, mid, end):
    left = words[start:mid]
    right = words[mid:end]

    left_sequence = 0
    right_sequence = 0

    for inception in range(start, end):
        if left_sequence >= len(left):
            words[inception] = right[right_sequence]
            right_sequence = right_sequence + 1
        elif right_sequence >= len(right):
            words[inception] = left[left_sequence]
            left_sequence = left_sequence + 1
        elif left[left_sequence] < right[right_sequence]:
            words[inception] = left[left_sequence]
            left_sequence = left_sequence + 1
        else:
            words[inception] = right[right_sequence]
            right_sequence = right_sequence + 1


def merge_sort(words, start=0, end=None):
    if end is None:
        end = len(words)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(words, start, mid)
        merge_sort(words, mid, end)
        merge(words, start, mid, end)


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return (first_string, second_string, False)

    first_string_ = "".join(merge_sort(first_string.lower()))
    second_string_ = "".join(merge_sort(second_string.lower()))

    return (first_string_, second_string_, first_string_ == second_string_)
