def toggle(text):

    result = ""

    for ch in text:

        if ch.isupper():
            result += ch.lower()

        elif ch.islower():
            result += ch.upper()

        else:
            result += ch

    return result


print(toggle("PyThOn123"))