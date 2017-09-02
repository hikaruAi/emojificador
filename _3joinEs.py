efile=open("onlyEmoji.txt","rt",encoding="utf-8")
elist=efile.readlines()
efile.close()

pfile=open("palabras.txt","rt",encoding="utf-8")
plist=pfile.readlines()
pfile.close()

ffile=open("emojis_es.txt","wt",encoding="utf-8")
ft=""
for i in range(0,827):
	ft+=plist[i].replace("\n","").lower()+" "+elist[i].replace(" ","")
ffile.write(ft)
ffile.close()