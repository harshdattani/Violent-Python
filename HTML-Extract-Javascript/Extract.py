import urllib2
from bs4 import BeautifulSoup
urlContent = urllib2.urlopen('<URL Name>').read()
soup = BeautifulSoup(urlContent)
imgTags = soup.findAll('img')
jsTags = soup.findAll('script')
print imgTags
i = 0
for jsTag in jsTags:
    i = i+1
    try:
        jsSrc = jsTag['src']
        print str(i)+' '+ jsSrc
        jsContent = urllib2.urlopen(jsSrc).read()
        jsFile = open('JS_'+str(i)+'.js', 'wb')
    	jsFile.write(jsContent)
    	jsFile.close()
    except:
        jsWrite = open('JS_'+str(i)+'.js', 'w')
        jsWrite.write(str(jsTag))
