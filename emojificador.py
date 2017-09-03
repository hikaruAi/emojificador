import time
import sys


file=open("emojis_es.txt","rt",encoding="utf-8")
lines=file.readlines()
file.close()
newlines=list()
banned=["de","con","la","el","ellos","mi","al","un","los","las","que","se","es","en"]
for l in lines:
	listapalabras=l.split(" ")
	for p in listapalabras:
		if len(p)<2 or p.lower() in banned:
			listapalabras.remove(p)
	listapalabras[-1]=listapalabras[-1].replace("\n","")
	newlines.append(listapalabras)
def emojizar(text):
	t0=time.time()
	textofinal=text[:]
	tf=""
	for palabra in text.split(" "):
		found=False
		if palabra.lower() in banned:
			print(palabra, "-> banned")
			found=True
		print("Palabra actual: ",palabra)
		for linea in newlines:
			if found:
				break
			for subpalabra in linea:
				if found:
					break
				if palabra.lower().replace(" ","").replace('"',"").replace(".","").replace(",","") == subpalabra.replace(" ",""):
					emoji=linea[-1]
					print("Found:", palabra, "->",linea)
					tf+=palabra+emoji+" "
					found=True
		if found==False:
			tf+=palabra+" "
	
	return tf
	print("Time:", time.time()-t0)

if __name__=="__main__":
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
