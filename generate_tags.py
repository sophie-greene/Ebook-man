import nltk
from ebooklib import epub 
from  comFunc import *
from IPython import get_ipython

d_dir = '/media/sf_lbuntu/calibre/'
txtfiles = find('*.txt', d_dir)

print (len(txtfiles))


f=open('keywords.txt')
keywords=list(s.replace('\n','') for s in f.readlines())
f.close()

try:
    booksTags=load_obj('booksTags')
except:
    booksTags={}
    save_obj(booksTags, 'booksTags')

cnt=0
for f in reversed(txtfiles):
    fl= open(f,'r')
    txt=fl.read().lower()
    fl.close()
    hist=nltk.FreqDist(txt.split())
    res=[[l,hist[l.strip()]] for l in keywords if l.strip() in hist.keys() ]
    tag=', '.join(r[0].strip() for r in res if r[1]>0)
    ff=f[:-3]+"epub" 
    name=f.split('/')[-1][:-4]
    if len(tag)>0 and name not in booksTags.keys():
        path=f.replace(f.split(os.sep)[-1],'')
        fm=path+"metadata.opf"
        get_ipython().system('ebook-meta "$ff" --tag "$tag" > /dev/null')
        get_ipython().system('ebook-meta "$ff" --to-opf "$fm" >/dev/null')
        booksTags[name]=' '.join(r[0]+": "+ str(r[1]) for r in res)
    print (f.split('/')[-1][:-4],res,tag)
    cnt+=1
    if cnt % 50 == 0:
        save_obj(booksTags, 'booksTags')
        tmp=booksTags.copy()
        tmp.update(load_obj('booksTags'))
        booksTags=tmp
        save_obj(booksTags, 'booksTags')

save_obj(booksTags, 'booksTags')
