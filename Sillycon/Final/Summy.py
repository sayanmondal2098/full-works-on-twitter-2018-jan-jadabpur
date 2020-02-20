import spacy
import textacy.extract
import urllib.request  
import bs4 as bs


# Load the large English NLP model
nlp = spacy.load('en_core_web_sm')
# nlp = spacy.load('')

raw_html = urllib.request.urlopen('https://en.wikipedia.org/wiki/London')  
raw_html = raw_html.read()

article_html = bs.BeautifulSoup(raw_html, 'lxml')

article_paragraphs = article_html.find_all('p')

article_text = ''

for para in article_paragraphs:  
    article_text += para.text


# Parse the document with spaCy
doc = nlp(article_text)

# Extract semi-structured statements
statements = textacy.extract.semistructured_statements(doc, "London")

# Print the results
print("Here are the things I know about London:")

for statement in statements:
    subject, verb, fact = statement
    print(f" - {fact}")