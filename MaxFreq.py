def maximum_frequency(text):

    maximum = 0
    answer = ""

    for ch in text:

        if text.count(ch) > maximum:

            maximum = text.count(ch)
            answer = ch

    return answer


print(maximum_frequency("programming"))