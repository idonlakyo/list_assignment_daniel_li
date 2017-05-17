def replace_characters(text_file, replaced_word, word_to_replace, index):
    front_of_list = text_file[:index]
    back_of_list = text_file[index+len(replaced_word):]
    
    if text_file[index] == replaced_word[0].upper():
        text_file = list(front_of_list) + list(word_to_replace[0].upper() + word_to_replace[1:]) + list(back_of_list)

    else:
        text_file = list(front_of_list) + list(word_to_replace) + list(back_of_list)

    return text_file

text = open("source.txt","r")
translated_text = open("translated.txt","w")
textlist = []
x = 0
punctuation = ['!', '.', '?']

while True:
    textline = text.readline()
    if textline == "":
        break
    else:
        textlist = textlist + list(textline)

while x != len(textlist) - 1:
    if textlist[x].lower() == "w" and textlist[x-1] == " ":
        textlist = replace_characters(textlist, "w", "v", x)

    elif textlist[x].lower() == "g" and (textlist[x+1] == "a" or textlist[x+1] == "o"):
        textlist = replace_characters(textlist, "g", "k", x)

    elif textlist[x].lower() == "s" and textlist[x+1].isalpha() == True:
        textlist = replace_characters(textlist, "s", "z", x)

    elif textlist[x].lower() == "t" and textlist[x+1] == "h":
        textlist = replace_characters(textlist, "th", "z", x)

    elif textlist[x].lower() == "a" and textlist[x+1] == " ":
        textlist = replace_characters(textlist, "a", "ein", x)

    elif textlist[x] == "I" and textlist[x+1] == " " and textlist[x-2] in punctuation:
        textlist = replace_characters(textlist, "I", "Argh! I", x)
        x += 6
    elif textlist[x].lower() == "p":
        textlist = replace_characters(textlist, "p", "b", x)

    elif textlist[x].lower() == "v":
        textlist = replace_characters(textlist, "v", "f", x)

    elif textlist[x].lower() == "b":
        textlist = replace_characters(textlist, "b", "p", x)



    x += 1
translated_text.write("".join(textlist))
