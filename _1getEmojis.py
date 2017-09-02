#!/usr/bin/python3
# coding: utf-8
import requests
import Translate

url=(r"https://emojipedia.org/food-drink/",
		r"https://emojipedia.org/people/",
		r"https://emojipedia.org/nature/",
		r"https://emojipedia.org/activity/",
		r"https://emojipedia.org/objects/")
def writer(text,append=True):
	if append:
		f=open("emojis.txt","at",encoding="utf-8")
	else:
		f=open("emojis.txt","wt",encoding="utf-8")
	f.write(text)
	f.close()

emojis=dict()
for u in url:
	print("Current url:",u)
	r=requests.get(u)
	r.close()
	source=r.text
	temp=source.split('<ul class="emoji-list">')[1].split("</ul>")[0]
	temp=temp.replace('"',"").replace('<li><a href=/',"").replace("-"," ").replace('/><span class=emoji>'," ").replace("face","")
	final=""
	for line in temp.split("\n"):
		i=line.find('</span>')
		line=line[:i]
		final=final+line+"\n"
	writer(final,True)
"""
finalText=""
t=Translate.Translate()
f=open("emojis.txt","rt",encoding="utf-8")
finalText=t.translate(f.read())
f.close()
fn=open("emojis_es.txt","wt",encoding="utf-8")
fn.write(text)
fn.close()"""

f=open("emojis.txt","rt",encoding="utf-8")
fText=f.read()
f.close()
wordsFile=open("onlywords.txt","at",encoding="utf-8")
emojiFile=open("onlyEmoji.txt","at",encoding="utf-8")
for line in fText.split("\n"):
	emoji=line[-2:]
	name=line[:-2]
	print(name,"---",emoji)