import urllib.request
from bs4 import BeautifulSoup
from owl.OWL import OWL


def getHtml(url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-agent', 'Mozilla/5.0')
        html = urllib.request.urlopen(req)
        return str(html.read())
    except:
        return ''


def getData(html, element, tag, attribute):
    text = BeautifulSoup(html)
    data = text.find_all(element, {attribute: tag})
    return data

def synonyms(word):
    listSynonyms = []
    html = getHtml('http://www.wordreference.com/sinonimos/' + word)
