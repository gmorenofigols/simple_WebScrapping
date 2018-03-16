#!/usr/bin/env python
import urllib2
import bs4


"""
Site structure where we info-scrapp is:
<div>
    <div>
        "Time left"
    <\div>
    <div>
        <h2> "Title" <\h2>
    <\div>
    <div>
        "Sinopsis"
    <\div>
    <div>
        <li> "Added book info" <\li>
    <\div>
<\div>
"""

class Client(object):
  """documentation TODO"""

  def get_web(self, url):
    f = urllib2.urlopen(url)
    html = f.read()
    f.close()
    return(html)

  def run(self):
    html = self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
    soup = bs4.BeautifulSoup(html, "lxml")

    title = soup.find("h2")
    clean_title = title.text.strip()

    #actual node is <h2> so .parent.parent to get self.<div> --> parent.<div>
    sinopsis = title.parent.parent.find_all("div")[2].text
    clean_sinopsis = sinopsis.strip()

    info = soup.find_all("li")

    print_results(clean_title, clean_sinopsis, info)

def print_results(title, sinopsis, info):
    print '\n',"Today's book in [https://www.packtpub.com/packt/offers/free-learning/] is:", '\n'
    print title, '\n'
    print sinopsis, '\n'
    #Sometimes, the site doesn't have any extra info
    if info is not None:
        for piece_of_info in info:
            print '-', piece_of_info.text, '\n'

if __name__ == '__main__':
  client = Client()
  client.run()
