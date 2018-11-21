import requests
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=44.9375&lon=-93.1406#.W-3YlpNKjp4")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/find_forecasts')
def find_forecasts():
	forecast_labels = [forecast.get_text() for forecast in soup.find_all(True, {'class':['forecast-label']})]
	forecast_texts = [forecast.get_text() for forecast in soup.find_all(True, {'class':['forecast-text']})]
	zip_list = tuple(zip(forecast_labels, forecast_texts))
	return render_template('index.html', zip_list=zip_list)


if __name__ == '__main__':
	app.run(debug=True)

