#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: awakenedhaki

'''
Parse Rosalind Bioinformatics Stronghold HTML table into list of problem IDs.
'''

import os
import sys
import re
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import List

url_list_id: str = 'http://rosalind.info/problems/list-view/'

def getHTML() -> str:
    '''
    Return text from HTML table of Bioinformatics Stronghold.
    '''
    r = urlopen(url_list_id)
    soup = BeautifulSoup(r, 'html.parser')
    problems = soup.find("table", class_="problem-list").get_text()
    return problems

def problemID(text: str) -> List[str]:
    '''
    Return problem ids from Bioinformatics Stronghold problems.
    '''
    pattern = re.compile("[A-Z]{3,4}")
    problem_ids = re.findall(pattern, text)
    return problem_ids

def removeDups(list_: list) -> list:
    '''
    Remove duplicates of problem IDs list.
    '''
    # no_dups is a list of elements without duplicates
    no_dups: list = []
    for element in list_:
        if element not in no_dups:
            no_dups.append(element)
    return no_dups

def fetchProblemIDs() -> List[str]:
    '''
    Fetch problem IDs from Bioinformatics Stronghold HTML table.
    '''
    problem_ids = removeDups(problemID(getHTML()))
    return problem_ids

def to_json(filename: str, problem_ids: List[str]) -> None:
    '''
    Save all problem IDs as a JSON file.
    '''
    with open(filename + '.json', 'w') as outfile:
        json.dump(problem_ids, outfile)
    return None

