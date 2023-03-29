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
    words_list_one = list(first_string.lower())
    words_list_two = list(second_string.lower())

    merge_sort(words_list_one)
    merge_sort(words_list_two)

    first_ordered_word = "".join(words_list_one)
    second_ordered_word = "".join(words_list_two)

    if first_ordered_word == "" or second_ordered_word == "":
        return (first_ordered_word, second_ordered_word, False)

    return (
        first_ordered_word,
        second_ordered_word,
        first_ordered_word == second_ordered_word,
    )
