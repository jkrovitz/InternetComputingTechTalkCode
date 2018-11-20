import requests


# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")\
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# print("This page has a status code of:", page.status_code)


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

# print(list(soup.children))

# print([type(item) for item in list(soup.children)])


# html = list(soup.children)[2]
# # print(html)

# body = list(html.children)[3]
# print(body)

# soup = BeautifulSoup(page.content, 'html.parser')
# soup.find_all('p')
# print(soup)

#find_all returns a list, so we'll have to loop through, or use list indexing to extract text. 
# print(soup.find_all('p')[0].get_text())

#To search by class and id: 
#print(soup.find_all('p', class_='outer-text'))


#find any tag with the class outer-text 
#print(soup.find_all(class_="outer-text"))


#search by id
# print(soup.find_all(id="first"))


