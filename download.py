import os
import tarfile
import urllib.request

def comment():
    url = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
    filepath = "D:/pythonWork/IMDb/aclImdb_v1.tar.gz"

    if not os.path.isfile(filepath):
        result = urllib.request.urlretrieve(url, filepath) # if file not exist, urllib.request.urlretrieve(A,B)
                                                           # will download A to B
        print('downloaded:', result)

    if not os.path.exists("D:/pythonWork/IMDb/acImdb"):
        tfile = tarfile.open("D:/pythonWork/IMDb/aclImdb_v1.tar.gz", 'r:gz')
        result = tfile.extractall('D:/pythonWork/IMDb/')
    