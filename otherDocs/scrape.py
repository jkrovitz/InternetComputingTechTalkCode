import bs4 as bs
import urllib.request
import requests
import json

# sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
# sauce = urllib.request.urlopen("https://www.yahoo.com/news/weather/").read()

# soup = bs.BeautifulSoup(sauce, 'lxml')

url = "https://www.yahoo.com/news/weather/"
lm_json = requests.get(url).json()
soup = BeautifulSoup(lm_json["content_html"])

#Returns the title of page 
# print(soup.title.text)


#The text method is better to use than string because text will return unicode. String is navitable. 
# It will not work if it has child tags inside of it. 
#print(soup.p.text) 



#print(soup.p.text)


#find all paragraph tags. 
#print(soup.find_all('p'))


# for paragraph in soup.find_all('p'):
#     print(paragraph.text)


# print(soup.get_text())


#for a tags, text returns the text of the tags, hrefs return the link.
# for url in soup.find_all('a'):
#     print(url.get('href'))



#-----------------------------



#We can specify a Beautiful soup object 
# nav = soup.nav

# print(nav)

# for url in nav.find_all('a'):
#     print(url.get('href'))


#In this case, we're grabbing the first nav tags that we can find (the navigation bar). You could also go for soup.body to get the body section, then grab the .text from there:
# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)



#Finally, sometimes there might be multiple tags with the same names, but different classes, and you might want to grab information from a specific tag with a specific class. For example, our page that we're working with has a div tag with the class of "body". We can work with this data like so:
# for div in soup.find_all('div', class_='body'):
#     print(div.text)




print(soup.get_text())

