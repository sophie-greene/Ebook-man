import os, fnmatch
from bs4 import BeautifulSoup
import pickle

#find all files in path satisfying pattern
def find(pattern,path=os.getcwd()):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

#write a variable obj to file name
def save_obj(obj, name ):
    with open( name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        
#read pickled variable
def load_obj(name ):
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f)

#remove html tags from string html     
def html2txt(html):
    soup = BeautifulSoup(html,"lxml")
    return soup.get_text()

# decide if a sentence which tag list is lst is a person's name
#example lst=[('Sophie','PERSON'),('Campell','LOCATION'),('Long', 'O'), ('Heatlerh', 'O')]
# will produce a True output
def isName(lst):
    cnt=0
    for m in lst:
        if m[1]!='O':
            cnt+=1
    if cnt >= len(lst)/2.0:   
        return True
    else:
        return False