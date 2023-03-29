def is_palindrome_recursive(word, low_index, high_index):
    if not len(word):
        return False
    elif word[low_index] != word[high_index]:
        return False
    elif high_index <= low_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
