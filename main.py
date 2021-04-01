#import spacy
#from spacy import displacy
from collections import Counter
import requests
import random
#from pprint import pprint

# model for NER
##nlp = en_core_web_sm.load()
#docu = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

#pprint([(X.text, X.label_) for X in doc.ents])
# streamlit_app.py

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Sundar Pichai is the CEO of Google."


def text_search(search_term):

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    SEARCHPAGE = str(search_term)

    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": SEARCHPAGE
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    if DATA['query']['search'][0]['title'] == SEARCHPAGE:
        #"Your search page '" + SEARCHPAGE + "' exists on English Wikipedia"
        return DATA['query']['search'][0]




def scraper(url):
	response = requests.get(
		url=url,
	)
	
	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title.text)

	allLinks = soup.find(id="bodyContent").find_all("a")
	random.shuffle(allLinks)
	linkToScrape = 0

	for link in allLinks:
		# We are only interested in other wiki articles
		if link['href'].find("/wiki/") == -1: 
			continue

		# Use this link to scrape
		linkToScrape = link
		break

	scraper("https://en.wikipedia.org" + linkToScrape['href'])
