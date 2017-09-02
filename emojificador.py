import time
import sys


file=open("emojis_es.txt","rt",encoding="utf-8")
lines=file.readlines()
file.close()
newlines=list()
for l in lines:
	listapalabras=l.split(" ")
	for p in listapalabras:
		if len(p)<2 or p in ("de","con","la","el","ellos","mi","al"):
			listapalabras.remove(p)
	listapalabras[-1]=listapalabras[-1].replace("\n","")
	newlines.append(listapalabras)
def emojizar(text):
	t0=time.time()
	textofinal=text[:]
	for palabra in text.split(" "):
		try:
			#print("Palabra actual: ",palabra)
			for linea in newlines:
				for palabraEnLinea in linea:
					if palabra.lower() in palabraEnLinea:
						emoji= linea[-1]
						#print(palabra, "->", emoji)
						textofinal=textofinal.replace(palabra,palabra +emoji)
						raise  StopIteration
		except  StopIteration as e:
			pass
	return textofinal
	print("Time:", time.time()-t0)

if __name__=="__main__":
	if len(sys.argv)>1:
		e=emojizar(sys.argv[1])
		print(e)
	else:
		try:
			import clipboard
			t=str(clipboard.paste())
			print("Text: ",t)
			if len(t)<1:
				print("Clipboard empty..")
				sys.exit()
			e=emojizar(t)
			print("Result copied to clipboard")
			clipboard.copy(e)
			print(e)
		except Exception as e:
			print(e)
			print("No input and no clipbaord module")
