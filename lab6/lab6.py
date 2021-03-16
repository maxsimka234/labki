import requests 
import bs4
from collections import namedtuple
obj_to_sort= namedtuple('objj' , ['name', 'num'])
def return_num(objj):
    return objj.num
f_url=open("url.txt","r")
f=open("site_info.txt","w", encoding='utf-8')
f_urls=open("site_urls.txt","w",encoding='utf-8')
f_tegs=open("site_tags_info.txt","w",encoding='utf-8')
f_words=open("site_words_info.txt","w",encoding='utf-8')

r=requests.get(f_url.read().strip())
f_url.close()
tags_list='''
!--...--	!DOCTYPE 	a	abbr	acronym	address	applet	area article	aside	 audio	b	base	basefont	bdi	bdo	big	
blockquote	body	br	button	canvas	caption center	Defines cite	code	col	colgroup	data	datalist	dddetails	
dfn	dialog	dir	div	dl	dt	em	 embed fieldset	figcaption	figure font	footer	form	frame	frameset	
h1 h2 h3 h4 h5 h6 head	header	hr	html	i	iframe	img	input	ins	kbd	label	legend	li	link	main	map	
mark meta	meter	nav noframes noscript object ol	Defines an ordered list optgroup option	 output	p	param	
picture	pre	progress	q	rp	rt	ruby	s	samp	script	section	select	small	source	span	strike	Defines 
strong	style	subsummary	sup	svg	table	tbody	tdtemplate	textarea	tfoot	th	thead	time	title	tr	track	
tt	u	ul var	video	wbr'''
print(r.ok," ",r.status_code)
soup=bs4.BeautifulSoup(r.text,"html.parser")

f.write("total url number :"+str(len(soup.find_all('a',href=True)))+"\n")
f.write("total img number :"+str(len(soup.find_all('img')))+"\ntext : \n")
f.write(soup.get_text())

for i in soup.find_all('a',href=True):
    f_urls.write(i["href"]+"\n")

tags__=[]
for tag_ in tags_list.split():
    if(len(soup.find_all(tag_))!=0):
        tags__.append(obj_to_sort(tag_,len(soup.find_all(tag_))))
tags__.sort(key=return_num)
tags__.reverse()
for tag_ in tags__ :
    f_tegs.write(tag_.name+": "+str(tag_.num)+"\n")    



words_=set(soup.get_text().split())
words=soup.get_text().split()
words__=[]
for i in words_:
    words__.append(obj_to_sort(i,words.count(i)))
words__.sort(key=return_num)
words__.reverse()
for word_ in words__ :
    f_words.write(word_.name+": "+str(word_.num)+"\n")    



f.close()
f_urls.close()
f_tegs.close()
f_words.close()