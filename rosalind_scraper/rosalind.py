#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: awakenedhaki

'''
Rosalind Bioinformatics Stronghold web scraper. Given a problem ID, a
README.md file is created with the contents of the specified problems.

The README.md is created within a directory named after the problem ID.
'''

import os
import sys
import re
import json
import click
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from typing import List, Tuple

home: str = os.getenv('HOME')
path: str = home + '/github/rosalind'

url_problem: str = 'http://rosalind.info/problems/'

try:
    os.chdir(path)
except FileNotFoundError:
    os.mkdir(home + '/github/rosalind')
    os.chdir(path)

def load_problemID() -> List[str]:
    '''
    Load problem ID json file.
    '''
    os.chdir(path + '/rosalind_scraper')
    with open('problem_ids.json', 'r') as infile:
        problem_ids = json.load(infile)
    os.chdir(path)
    return problem_ids

def addNewLine(list_: List[str], str_, sub = 0, add_ = 0) -> List[str]:
    '''
    Insert two two \n at str_ index or str_ index - sub + add.
    '''
    index: int = list_.index(str_) - sub + add_
    list_.insert(index, '\n\n')
    return list_

def suggestCorrection(ID: str) -> None:
    '''
    If HTTPError, provide possible correct ID spelling options to user.
    '''
    problem_ids: List[str] = load_problemID()
    input_id: List[str] = sorted(list(ID.upper()))
    for id in problem_ids:
        if input_id == sorted(list(id)):
            new_id: str = input(f'\nDid you mean {id}? [y/n] ')
            if new_id == 'y':
                makeFile(id)
                break
    else:
        print('\nID not found.')

def parseHeader(html: BeautifulSoup) -> str:
    '''
    Obtain header from problem site.
    '''
    header: str = html.find('h1').get_text()
    parsed_header: str = ' '.join(header.split()[:-3])
    return parsed_header

def parseProblem(html: BeautifulSoup) -> str:
    '''
    Obtain problem statement, and separate components with newlines.
    '''
    problem: str = html.find('div', class_='problem-statement').get_text()
    # Problem description begins at index i + 7 (length of 'Problem')
    i: int = problem.index('Problem') + 7
    problem: str = problem[i:]
    # Add new line to Given, Return, Sample Dataset
    parsing: List[str] = problem.split()
    addNewLine(parsing, 'Return:')
    addNewLine(parsing, 'Dataset', sub=1)
    addNewLine(parsing, 'Dataset', add_=1)
    addNewLine(parsing, 'Output', sub=1)
    addNewLine(parsing, 'Output', add_=1)
    if 'Note' in parsing:
        addNewLine(parsing, 'Note')
    # Final text
    parsed_problem: str = ' '.join(parsing)
    return parsed_problem

def parseTopic(html: BeautifulSoup) -> str or None:
    '''
    Obtain problem topic as string, otherwise return None.
    '''
    try:
        topic: str = html.find('p', class_='topics').get_text()
        parsed_topic: str = ' '.join(topic.split()[1:])
        return parsed_topic
    except AttributeError:
        return None

def fetchProblem(problem_id: str) -> str:
    '''
    Return Bioinformatics Stronghold specified problem ID description.
    '''
    r = urlopen(url_problem + problem_id)
    soup = BeautifulSoup(r, 'html.parser')
    header: str = parseHeader(soup)
    topics: str or None = parseTopic(soup)
    problem: str = parseProblem(soup)
    return (header, topics, problem)

def makeFile(problem_id: str) -> None:
    '''
    Create README.md, with problem content in new directory.
    '''
    file_content: Tuple[str] = fetchProblem(problem_id)
    header, topics, problem = file_content
    # Create directory {problem_id}.upper()
    try:
        os.chdir(f'{problem_id.upper()}')
    except FileNotFoundError:
        os.mkdir(f'{problem_id.upper()}')
        os.chdir(f'{problem_id.upper()}')
    with open(f'README.md', 'w') as outfile:
        outfile.write(f'## {header}\n\n')
        if topics is None:
            outfile.write('No listed topics.\n\n')
        else:
            outfile.write(f'Topics: {topics}\n\n')
        outfile.write(f'{problem}')

@click.command(help='''Creates a Markdown file for a given Rosalind 
               Bioinformatics Stronghold problem ID.''')
@click.argument('problem_id')
def main(problem_id):
    '''
    Calls makeFile to create markdown file with requested problem ID.
    '''
    try:
        makeFile(problem_id)
    except HTTPError:
        suggestCorrection(problem_id)

if __name__ == '__main__':
    main()
