f=open("emojis.txt","rt",encoding="utf-8")
fText=f.read()
f.close()
wordsFile=open("onlywords.txt","at",encoding="utf-8")
emojiFile=open("onlyEmoji.txt","at",encoding="utf-8")
for line in fText.split("\n"):
	if len(line)<2:
		pass
	palabras=line.split(" ")
	emoji=str(palabras[-1])
	name=""
	for p in palabras[:-1]:
		name=name+p+" "
	wordsFile.write(name+"\n")
	emojiFile.write(emoji+"\n")
wordsFile.close()
emojiFile.close()