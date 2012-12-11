import urllib2
from bs4 import BeautifulSoup
from threading import Thread

class tt(Thread):
    def run(self):
        global fila
        global alreadyVisited
        while len(fila) > 0:
            nxt = fila.pop()
            url = nxt.get('href')
            if not url or not url.startswith('http://') or url in alreadyVisited:
                continue
            alreadyVisited.add(url)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print len(fila), self.getName()
            print url
            document = response.read()
        
        
            soup = BeautifulSoup(document)
            links = soup.findAll('a')

            fila.extend([link for link in links if link.get('href') and link.get('href').find('g1') > 0])
    



url = "http://www.g1.com.br"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()


soup = BeautifulSoup(document)
links = soup.findAll('a')

fila = []
fila.extend([link for link in links if link.get('href') and link.get('href').find('g1') > 0])
alreadyVisited = set()
alreadyVisited.add(url)

for i in range(0,32):
    print "Thread %d" % i
    tt().start()
