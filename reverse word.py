def reverse_word(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word


word = input("Enter a word to reverse: ")
reversed_word = reverse_word(word)
print(f"The reversed word is: {reversed_word}")
