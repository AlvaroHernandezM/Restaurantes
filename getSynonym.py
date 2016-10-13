import urllib.request
from bs4 import BeautifulSoup


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
    data = text.find_all(element, {tag: attribute})
    return data

def synonyms(word):
    listSynonyms = []
    elements = []
    html = getHtml('http://sinonimos.woxikon.co/es/' + word)
    data = getData(html, 'div', 'class', 'synonyms-list-group')
    for element in data:
        listSynonyms.append(element.find('b').getText())
    return listSynonyms