import requests
from bs4 import BeautifulSoup

def getPage(gameName):
	gameName = gameName
	url = "https://www.allkeyshop.com/blog/catalogue/search-"+gameName+"/"
	try:
		page = requests.get(url)
		if page.status_code == 200:
			soup = BeautifulSoup(page.content, 'html.parser')
			a = soup.find_all('div', class_="search-results-row-price")
			price = a[0].get_text()
			priceTag = price.split()
			print("The lowest price you can get, right now is: "+ priceTag[0])
		else:
			print("Something wrong just happened, try again")
			inputName()
	except:
		print("Problem getting the page, please check your internet connection")
		inputName()
	

def normalizeName(game):
	game = game
	gameName = ""
	for i in game:
		if i == " ":
			i = "-"
			gameName = gameName + i
		else:
			gameName = gameName + i
	getPage(gameName)


def inputName():
	game = input("Choose the game: ")
	normalizeName(game)


inputName()
