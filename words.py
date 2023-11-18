def print_upper_words(words):
    """Turns words in a list into all uppercase and returns each word"""
    for word in words:
        yell = word.upper()
        print(yell)

def print_only_e(words):
    """Uppercases each word but only returns words that start with the letter 'e' """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_your_letters(words, letters):
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
                