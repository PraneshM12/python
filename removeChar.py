def remove(text, target):

    result = ""

    for ch in text:

        if ch != target:
            result += ch

    return result


print(remove("banana", "a"))