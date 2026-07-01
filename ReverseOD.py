def rev_word(sentence):
    word = sentence.split()
    return " ".join(word[::-1])
text = "Hai Hello, What's going on today?"
print(rev_word(text))