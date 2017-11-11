from bs4 import BeautifulSoup as soup
from urllib2 import urlopen
from tabulate import tabulate
import webbrowser
import sys


#if the search word is too small, throw error
if(len(sys.argv) < 2):
    print("Enter valid string")
    exit()

#get the search word
string_query = sys.argv[1].replace(" ","-")
my_url = "https://listado.mercadolibre.com.ve/" + string_query;


final_list = []

i= 1;
flag = True
while flag:
	client = urlopen(my_url)
	page_html = client.read()
	client.close()
	page_soup = soup(page_html, "html.parser")
	all_items = page_soup.findAll("li", { "class" : "results-item article stack item-without-installmets" })
	for item in all_items:
		info = []
		item_info = item.findAll("div", {"class" : "item__info"})
		item_info = item_info[0]
		item_title = item_info.findAll( "span", {"class": "main-title"})[0].contents[0]
		item_price = item_info.findAll( "span", {"class": "price-symbol"})[0].contents[0] + " " + item_info.findAll( "span", {"class": "price-fraction"})[0].contents[0]
		item_image = item.findAll("div",{"class" : "image-content"})[0].a.findAll('img',{"src":True})[0]["src"] if len(item.findAll("div",{"class" : "image-content"})[0].a.findAll('img',{"src":True}))>0 else item.findAll("div",{"class" : "image-content"})[0].a.img["data-src"]
		item_link = item.findAll("div",{"class" : "image-content"})[0].a["href"]
		item_status = item.findAll("div",{"class" : "item__condition"})[0].contents[0]
		final_list.append([ i, item_title, item_price, item_status, item_link, item_image])
		i = i +1
	next_url = page_soup.findAll("li", {"class" : "pagination__next"})
	end = page_soup.findAll("li", {"class" : "pagination__next pagination--disabled"})
	if len(end)>0:
		flag = False
	else:
		my_url = next_url[0].a["href"];
		print my_url


#headers before the table
print_headers = ['Number','Title', 'price', 'status','link', 'image']

#print the table with tabulate
body = tabulate(final_list, headers=print_headers, tablefmt="html")

f = open('list.html','w')
f.write(body.encode('utf-8'))
f.close()

webbrowser.open_new("list.html")
