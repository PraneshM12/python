def analyze(text):

    upper = lower = digit = special = 0

    for ch in text:

        if ch.isupper():
            upper += 1

        elif ch.islower():
            lower += 1

        elif ch.isdigit():
            digit += 1

        else:
            special += 1

    print("Upper:", upper)
    print("Lower:", lower)
    print("Digits:", digit)
    print("Special:", special)


analyze("Python@2025!")