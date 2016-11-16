import os, fnmatch
from bs4 import BeautifulSoup
import pickle
import re, math
from collections import Counter

WORD = re.compile(r'\w+')

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
        pickle.dump(obj, f,protocol=2)
        
#read pickled variable
def load_obj(name ):
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f, encoding="utf-8")
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
#similiarity

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)
