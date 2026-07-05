def unique(text):

    seen = set()

    for ch in text:

        if ch in seen:
            return False

        seen.add(ch)

    return True


print(unique("python"))