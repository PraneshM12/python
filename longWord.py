def longest_word(sentence):

    words = sentence.split()

    longest = words[0]

    for word in words:

        if len(word) > len(longest):
            longest = word

    return longest


text = "Python programming is amazing"

print(longest_word(text))