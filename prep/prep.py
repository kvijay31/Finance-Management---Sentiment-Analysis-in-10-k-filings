import os
import re
import json
import pandas as pd
from bs4 import BeautifulSoup

def load_sec_filing(acc_nr, path, bs=True):
    with open(os.path.join(path, f'{acc_nr}.html'), 'r') as f:
        contents = f.read()
    if bs:
        soup = BeautifulSoup(contents, 'lxml')
        return soup
    return contents

def load_bs(contents):
    return BeautifulSoup(contents, 'lxml')

def clean_filing(soup):
    # remove all table tags from document
    for s in soup.select("table"):
        s.extract()
        
    # only keep document tag (removes metadata)
    doc = False
    for s in soup.select("document"):
        document = s
        doc = True
        break
    if not doc:
        document = soup
    document = document.get_text()
    document = re.sub(r"[\n|\s]", " ", document)
    # document = re.sub(r"[^\s|\w|\d]", " ", document)
    return document