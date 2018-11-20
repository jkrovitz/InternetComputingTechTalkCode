import requests
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=44.9375&lon=-93.1406#.W-3YlpNKjp4")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
from flask import Flask, render_templtea

app = Flask(__name__)





# for div in divs:
#     inner_text = div.text
#     strings = inner_text.split("\n")
#     print strings[0] ## I want this to print just {TITLE}

# soup = BeautifulSoup(page.content, 'html.parser')
# seven_day = soup.find(id="seven-day-forecast")
# forecast_items = seven_day.find_all(class_="tombstone-container")
# for div in forecast_items:
# 	print(div.text)
# divs = seven_day.findAll({ "tombstone-container" : "text" })
# for div in divs:
# 	print(div)
#     # inner_text = div.text
#     # strings = inner_text.split("\n")
#     # print(strings[0]) ## I want this to print just {TITLE}

# tonight = forecast_items[0]

# print(forecast_items)
# print(tonight.prettify())

# print(soup.find_all(class_="period-name"))

# def find_period_name():
# 	for p in soup.find_all('p', class_='period-name'):
# 		period_name = p.text
# 		return period_name 


# def find_short_desc():
# 	for p in soup.find_all('p', class_='short-desc'):
# 		short_desc = p.text
# 		return short_desc 

# def find_temp():
# 	for p in soup.find_all('p', class_='temp'):
# 		temp = p.text
# 		return temp



# def find_forecast_label():
# 	for l in soup.find_all('div', class_='forecast-label'):
# 		forecast_label = l.text
# 		return forecast_label
	
# def find_forecast_text():
# 	for t in soup.find_all('div', class_='forecast-text'):
# 		forecast_text = t.text
# 		return forecast_text
		
# def find_forecast():

# 	newForecast.append(forecast_label_result + ': ' + forecast_text_result + '\n')
	

@app.route('/')
@app.route('/find_forecasts')
def find_forecasts():

	# for forecast in soup.find_all(True, {'class':['forecast-label', 'forecast-text']}):
	# 	forecast_text = forecast.text 
	return render_template('index.html', soup=soup)

# find_forecasts()


# def print_weather_info():
# 	for p in soup.find_all('p', class_='period-name'):
# 		period_name = p.text
# 	for p in soup.find_all('p', class_='short-desc'):
# 		short_desc = p.text

# 	for p in soup.find_all('p', class_='temp'):
# 		temp = p.text			
# 		print(period_name + ':', short_desc, temp, '\n')


# print_weather_info()


# def print_weather_descriptions():
# 	for img in soup.findAll('img', title=True):
# 		print(img['title'], '\n')
# 		if img['title'] is None:
# 			if 'title' in img:
# 				img['title'] = img['title']
# 				print(img['title'], '\n')


# print(soup.find_all(class_="forecast_label"))


# print_weather_descriptions()


if __name__ == '__main__':
	app.run(debug=True)

