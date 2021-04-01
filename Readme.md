Wikipedia fetching and task assignment.
I was asked to make the following:
- A scraper (from Wiki API)
- Spacy model to perform NER(en_core_web_sm)
- Streamlit display(Frontend)

Some challenges I faced:
It wasn't made clear how flask will be included in this project, streamlit does most of the work,
unless the assignment requires to make a back-end where all the search queries(previous), keep getting stored, but looking at the time given, I thought that would be unnecessary. Would be happy to make any changes necessary for the assignment. The question did not make it clear.

app.py:
Has all the neccessary packages imported and being used, Takes in an input from the user(search word), and serves a snippet with NER performed on it. Would store necessary functions. NER is performed using en_core_web_sm

Directions to use:
Just enter any term you want to search about, and some general details from the wikipedia api will be served, (wikimedia.action).
There was no mention of the maximum word limit for data to be scrapped, also the Sample flow mentioned use of Flask API, but streamlit was more than enough, as we had json response from wikipedia. I would be happy to make any suitable changes. But the live url is getting the task done, like it was mentioned.

Live URL:https://wiki-ner.herokuapp.com/

Some Samples of the website:
![image](https://user-images.githubusercontent.com/60900660/113256386-bf076b80-92e6-11eb-870d-14f6dddcf599.png)
