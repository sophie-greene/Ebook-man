import os
import isbnlib
import string
import comFuncs
from comFuncs import *
from isbnlib.config import add_apikey
APIKEY="2E7FE5A4"
import os
import string
SERVICE = 'isbndb'
#register your key
add_apikey(SERVICE, APIKEY)
print "api initialised"
def getISBNmeta(title,author):
    #isbn=isbnlib.isbn_from_words(title+" by " +author)
    try:
        return isbnlib.goom(title+" " +author)
    except:
        return
        #print "service unavailable"
def getFileIsbnMeta(f,smscr):
    print "start"
    fp,ff= os.path.split(f)
    fn, fext = os.path.splitext(ff)
    seri=''
    sm=0
    mtd=None
    sp=fn.split()
    if len(sp)>4:
        auth=sp[-2:]
        tit=sp[:-2]
    elif len(sp) >1:
        auth=fn.split()[-1:]
        tit=fn.split()[:-1]
    else:
        return "no meta"
    
    if fn.count(' - ')==1:
        tit,auth=fn.split(' - ')
    elif fn.count(' - ')==2:
        seri,tit,auth=fn.split(' - ')
        
    author=''.join(l for l in ' '.join(auth.split()) if l in string.ascii_letters+" .")
    if tit.count('_ ')==1:
            tit=' '.join(tit.split('_ ')[0].split())
    title=''.join(l for l in ' '.join(tit.split()) if l in string.ascii_letters+string.digits+" .,&")
    #print title,'..... ....',author
    metad =getISBNmeta(title,str(author))
    if metad !=None and len(metad)>0: 
        for md in metad:
            #print md
            authsim=similarity(md['Authors'][0].encode('ascii','ignore'),str(author))
            titsim=similarity(md['Title'].encode('ascii','ignore'),str(title))
            #print titsim,authsim
            if titsim+authsim >sm:
                sm=titsim+authsim
                mtd=md
    #if no data found switch title and author
    metad =getISBNmeta(author,str(title))
    if metad !=None and len(metad)>0: 
        for md in metad:
            authsim=similarity(md['Authors'][0].encode('ascii','ignore'),str(title))
            titsim=similarity(md['Title'].encode('ascii','ignore'),str(author))
            #print titsim,authsim
            if titsim+authsim >sm:
                sm=titsim+authsim
                mtd=md
    # if no data found try seri, auth ,title  combinaton
    if seri !='':
        metad =getISBNmeta(title,str(seri))
        if metad !=None and len(metad)>0: 
            for md in metad:
                authsim=similarity(md['Authors'][0].encode('ascii','ignore'),str(seri))
                titsim=similarity(md['Title'].encode('ascii','ignore'),str(title))
                #print titsim,authsim
                if titsim+authsim >sm:
                    sm=titsim+authsim
                    mtd=md
        metad =getISBNmeta(seri,str(author))
        if metad !=None and len(metad)>0: 
            for md in metad:
                authsim=similarity(md['Authors'][0].encode('ascii','ignore'),str(author))
                titsim=similarity(md['Title'].encode('ascii','ignore'),str(seri))
                #print titsim,authsim
                if titsim+authsim >sm:
                    sm=titsim+authsim
                    mtd=md    
        metad =getISBNmeta(seri,str(title))
        if metad !=None and len(metad)>0: 
            for md in metad:
                authsim=similarity(md['Authors'][0].encode('ascii','ignore'),str(title))
                titsim=similarity(md['Title'].encode('ascii','ignore'),str(seri))
                #print titsim,authsim
                if titsim+authsim >sm:
                    sm=titsim+authsim
                    mtd=md
        metad =getISBNmeta(author,str(seri))
        if metad !=None and len(metad)>0: 
            for md in metad:
                authsim=similarity(md['Authors'][0].encode('ascii','ignore'),str(seri))
                titsim=similarity(md['Title'].encode('ascii','ignore'),str(author))
                #print titsim,authsim
                if titsim+authsim >sm:
                    sm=titsim+authsim
                    mtd=md               
    if sm >smscr and mtd !=None:
        return fn,fp,mtd,sm
    return "NO meta"   