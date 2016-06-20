import urllib2
import urllib
import xmltodict
import os
import string
#query contains book name and author
# key is the goodread API key
#path is location where the cover image shall be stored
def getGRMeta(title,author,key,path):
    urlstring="https://www.goodreads.com/search/index.xml?key="+key+"&q="+query.replace(" ","+")
    #print urlstring
    try:
        url=urllib2.urlopen(urlstring)
        data=xmltodict.parse(url.read())
        if len(data)>0:
            meta=data[u'GoodreadsResponse'][u'search'][u'results'][u'work'][0][u'best_book']
            dictt={}
            
            dictt['title']=str(meta[u'title'])
            dictt['author']=str(meta[u'author'][u'name'])
            fileName=dictt['author']+" - "+dictt['title']
            dictt['imageL']=path+dictt['author']+" - "+dictt['title']+".jpg"
            img=str(meta[u'image_url'])
            dictt['imageR']=img
            #urllib.urlretrieve(img,dictt['imageR'])
            return fileName,dictt
        else:
            return False
    except:
        return False