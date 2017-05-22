#-------------------------------------------------------------------------------
# Name:		<filename>.py
# Purpose:		Translates a given source text into english with a german accent
#
# Author:		Li. D
#
# Created:		12/05/2017
#------------------------------------------------------------------------------


def replace_characters(text_list, replaced_word, word_to_replace, index):
    """
    :param text_list: list - The list of the file that will be translated
    :param replaced_word: str - The word going to be replaced
    :param word_to_replace: str - The word that is going to replace a word
    :param index: int - The index in which the word going to be replace is at
    :return: list - The list of the file with a single translation completed
    """
    # Create two lists, one for everything before the word being replaced and one for everything after
    front_of_list = text_list[:index]
    back_of_list = text_list[index+len(replaced_word):]

    # Checks if the word being replaced is capitalized
    if text_list[index] == replaced_word[0].upper():
        # Adds front of list and back of list with the new word capitalized
        text_list = list(front_of_list) + list(word_to_replace[0].upper() + word_to_replace[1:]) + list(back_of_list)

    else:
        # Does same thing but the new word is lowercase
        text_list = list(front_of_list) + list(word_to_replace) + list(back_of_list)

    # Return the list with the changed word
    return text_list

# Opens the file going to be translated, initialize other needed variables
text = open("source.txt","r")
translated_text = open("translated.txt","w")
text_list = []
x = 0

while True:
    # Reads a line and checks if it is empty, if so, it breaks
    textline = text.readline()
    if textline == "":
        break
    else:
        # Otherwise, add it to a list as letters
        text_list += list(textline)

# Goes through everything looking for letters/words to be replaced
# Condition is dynamic, since length of list might change
while x != len(text_list) - 1:
    if text_list[x].lower() == "w" and text_list[x-1] == " ":
        text_list = replace_characters(text_list, "w", "v", x)

    elif text_list[x].lower() == "g" and (text_list[x+1] == "a" or text_list[x+1] == "o"):
        text_list = replace_characters(text_list, "g", "k", x)

    elif text_list[x].lower() == "s" and text_list[x+1].isalpha() == True:
        text_list = replace_characters(text_list, "s", "z", x)

    elif text_list[x].lower() == "t" and text_list[x+1] == "h":
        text_list = replace_characters(text_list, "th", "z", x)

    elif text_list[x].lower() == "a" and text_list[x+1] == " ":
        text_list = replace_characters(text_list, "a", "ein", x)

    elif text_list[x] == "I" and text_list[x+1] == " " and text_list[x-2] in ["!", "?", "."]:
        text_list = replace_characters(text_list, "I", "Argh! I", x)
        x += 6
    elif text_list[x].lower() == "p":
        text_list = replace_characters(text_list, "p", "b", x)

    elif text_list[x].lower() == "v":
        text_list = replace_characters(text_list, "v", "f", x)

    elif text_list[x].lower() == "b":
        text_list = replace_characters(text_list, "b", "p", x)

    # Add 1 to counter
    x += 1

# Writes the new translated text to a new file
translated_text.write("".join(text_list))