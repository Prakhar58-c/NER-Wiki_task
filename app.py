import spacy
from spacy import displacy
from collections import Counter
import streamlit as st
import spacy_streamlit
import re
import requests


def text_search(search_term):
    # Scraper function
    S = requests.Session()
    #link for Wikipedia api for requests
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
    return DATA['query']['search'][0]['snippet']





keyword = st.text_input('Enter a keyword for search')
#keyword = str.replace(keyword, ' ', '_')

# use this url for scraping data 

Text = ''
flag = True


# get URL
Text = str(text_search(str(keyword)))

Text = re.sub('<span class=\"searchmatch\">.*?</span>', '', Text)

#Text.replace("<span class=\"searchmatch\">", "")
#Text.replace('</span>','')

if Text == '':
    flag = False


if flag:
    spacy_streamlit.visualize(["en_core_web_sm"], Text)
else:
    st.write('Type in a common search term, No results found in previous')
