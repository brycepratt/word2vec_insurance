import numpy as np
import csv

def count_chars(input):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lowercase = input.lower()
    dict = {}
    for a in alphabet:
        dict[a] = 0
    for char in lowercase:
        dict[char] += 1
    res = []
    for char in alphabet:
        res.append(dict[char])
    return res


def write_one_hot(input, type):
    filename = 'decoding/'+type+'.csv'

    with open(filename, 'w', newline=''):
        
