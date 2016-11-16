import os,glob,fnmatch,re
def findFiles(path,pattern):

    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        result += [os.path.join(root, j) for j in files if re.match(fnmatch.translate(pattern), j, re.IGNORECASE)]
    return result
    