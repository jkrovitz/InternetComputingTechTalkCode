import requests
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=44.9375&lon=-93.1406#.W-3YlpNKjp4")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/find_forecasts')
def find_forecasts():
	return render_template('index.html', soup=soup)


if __name__ == '__main__':
	app.run(debug=True)

