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
        if textlist[x] == "A"
            textlist[x] = "E"
        if textlist[x] == "a":
            textlist[x] = "e"
        temptext = textlist[x+1:]
        textlist[x+1] = "i"
        textlist[x+2] = "n"
        for i in range(len(textlist[x+3:])):
            textlist[i-2] = templist[i]
    x += 1
text.seek(0)
text.write("".join(textlist))
