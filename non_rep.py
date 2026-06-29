def first_non_repeating(s):

    for ch in s:

        if s.count(ch) == 1:
            return ch

    return None


text = "aabbcddee"

print(first_non_repeating(text))