from bs4 import BeautifulSoup
import urllib
import nltk

link = 'http://www.bartleby.com/124/'
file = open('index.html', 'r')
soup = BeautifulSoup(file, 'html.parser')

dt = soup.find_all('a')

for dti in dt:
    href = dti['href']
    link = 'http://www.bartleby.com/124/' + href
    fname = "speeches/" + href.split('.')[0] + '.txt'
    print fname, link
    r = urllib.urlopen(link).read()
    speechSoup = BeautifulSoup(r, 'html.parser')
    f = open(fname, 'a+')
    [s.extract()
     for s in speechSoup(['style', 'script', '[document]', 'head', 'title'])]
    f.write(speechSoup.get_text().encode('ascii', 'ignore').decode('ascii'))
    # print speechSoup.td
