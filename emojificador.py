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
		if len(p)<1 or p.lower() in banned:
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
			tf+= palabra+" "
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
	tf= tf.replace("b","🅱").replace("B","🅱").replace("p", "🅿").replace("P", "🅿").replace("gg","🅱🅱")
	return tf
	print("Time:", time.time()-t0)

if __name__=="__main__":
	try:
		import clipboard
		#t="""La computadora dió una señal roja de atención refiriendose a un error en la información introducida o con los resultados obtenidos al compararse con las normas establecidas. La oficina de mantenimiento realiza un chequeo, pero la computadora estaba en perfecto estado. El director de operaciones de IBM preguntó cual era el problema entonces siendo la respuesta: “ Detectamos que falta un día en el universo del tiempo transcurrido en la historia”."""
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
