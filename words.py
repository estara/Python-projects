def print_upper_words(words, letters):
    #print out uppercase any words that start with a letter in the list
    for word in words:
        for letter in letters:
            if word[0].lower() == letter.lower():
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "y"})