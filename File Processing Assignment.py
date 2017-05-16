text = open("source.txt","r+")
textlist = []
x = 0
while True:
    textline = text.readline()
    if textline == "":
        break
    for i in range(len(textline)):
        textlist.append(textline[i])
while x != len(textlist) - 1:
    if textlist[x] == "w":
        print("w")
        textlist[x] = "v"
    if textlist[x].lower() == "t" and textlist[x+1] == "h":
        print("h")
        if textlist[x] == "T":
            textlist[x] = "Z"
        else:
            textlist[x] = "z"
        textlist.remove(textlist[x+1])
    if textlist[x].lower() == "a" and textlist[x+1] == " ":
        front_of_list = textlist[:x]
        back_of_list = textlist[x+1:]
        if textlist[x].lower() == "A":
            textlist = front_of_list + ['E','i','n'] + back_of_list
        else:
            textlist = front_of_list + ['e','i','n'] + back_of_list
    x += 1
text.seek(0)
text.write("".join(textlist))
