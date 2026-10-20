# Ambianese translator

code_words = ['lucozade', 'office', 'car', 'cornflakes', 'soup']

# Take input from the user and translate it to the custom Ambianese language.

# get original text from user
original_text = input("Enter text to translate to Ambianese: ")

# split the text into words
words = original_text.split()

# define a function to translate each word to Ambianese
def translate_to_ambianese(word):
    # If the element is a whole number, prefix it with a dollar sign
    if word.isdigit():
        return f"${word}"

    # If the element contains the substring ‘lunch’, replace the entire word with the string ‘1:30PM’
    if 'lunch' in word:
        #replace the word beginning with 'lunch' with '1:30PM' as the new word
        return '1:30PM'


    # If the element matches one of the words in a list of code words, replace the word with ‘Ambiance’
    if word in code_words:
        return "Ambiance"

    # If the length of the word is greater than 8 characters, replace the word with ‘Ambiance’
    if len(word) > 8:
        return "Ambiance"


    # For all other words, check if the first character in the word is a lowercase letter.
    # If it is, then convert it to uppercase. You should use chr() and ord() to solve this.
    # The ord() function returns the code point of a character, and the chr() function returns
    # the character represented by a code point. The difference between the code points of a
    # lowercase character and its corresponding uppercase version is always 32.
    # Case conversion methods shouldn’t be used here. Remember, you are only converting the first character to uppercase.

    if 'a' <= word[0] <= 'z':
        word = chr(ord(word[0]) - 32) + word[1:]
    return word


# The new list containing the newly created strings should now be converted back to a sentence using the join method

translated_words = [translate_to_ambianese(word) for word in words]
translated_text = " ".join(translated_words)
print(translated_text)



#Testing the code:
# To test the code, the following sentence should be entered as user input:
# 10 for the breakfast. I hope that my cornflakes at lunchtime will be cheaper!
#
# The output at the end of code execution should be:
# $10 For The Ambiance I Hope That My Ambiance At 1:30PM Will Be Cheaper!
#
# Actual output:
# $10 For The Ambiance I Hope That My Ambiance At 1:30PM Will Be Cheaper!

# Tips:
# •	isdecimal() can be used to determine if the string is a decimal string
# •	find() can be used to search for the substring ‘lunch’ within a string
# •	The in operator will allow you to easily check if an element is in a list (or other complex data type)
# •	To convert the first character of all remaining words to uppercase, you will need to use indexing
# (to reference the first character that needs manipulating) and slicing(to reference the remainder of the word
# that should remain unchanged). You can then concatenate the strings together again after the case conversion,
# appending this new string to the list