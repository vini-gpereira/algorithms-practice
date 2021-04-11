def reverse_words(sentence):    # sentence here is an array of characters
    reverse = []
    word = []

    for i in range(len(sentence) - 1, -1, -1):
        char = sentence[i]
        if char == ' ':
            reverse = word + [" "] + reverse
            word = []
        else:
            word.append(char)
    
    if word != "":
        reverse = word + [" "] + reverse

    return reverse

if __name__ == "__main__":
    sentence = "Hello world"
    print(''.join(reverse_words([ char for char in sentence ])))
