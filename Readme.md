Wikipedia fetching and task assignment.
I was asked to make the following:
- A scraper (from Wiki API)
- Spacy model to perform NER(en_core_web_sm)
- Streamlit display(Frontend)

Some challenges I faced:
It wasn't made clear how flask will be included in this project, streamlit does most of the work,
unless the assignment requires to make a back-end where all the search queries(previous), keep getting stored, but looking at the time given, I thought that would be unnecessary.

Stream.py:
Has all the neccessary packages imported and being used, Takes in an input from the user(search word), and serves a snippet with NER performed on it. Would store necessary functions. Was not used much.

app.py:
Have all the flask functionality, to deal with scraping from the wiki-api
