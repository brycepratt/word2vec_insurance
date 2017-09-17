import numpy as np
import csv


def count_chars(inp):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lowercase = inp.lower()
    dict = {}
    for a in alphabet:
        dict[a] = 0
    for char in lowercase:
        if char.isalpha():
            dict[char] += 1
    res = []
    for char in alphabet:
        res.append(dict[char])
    return res


def read_data(filename):
    name = []
    sex = []
    lat = []
    long = []
    birth = []
    product = []
    coverage = []
    premium = []
    plan = []
    with open(filename, 'r') as csv_file:
        for row in csv_file:
            temp = row.split(',')
            name.append(count_chars(temp[0]))
            sex.append(sex_format(temp[1]))
            lat.append(lat_long_format(temp[2]))
            long.append(lat_long_format(temp[3]))
            birth.append(birth_format(temp[4]))
            product.append(temp[5])
            coverage.append(temp[6])
            premium.append(temp[7])
            plan.append(temp[8])
    return name, sex, lat, long, birth, product, coverage, premium, plan


def sex_format(inp):
    if inp == 'M':
        return [1, 0]
    else:
        return [0, 1]


def lat_long_format(inp):
    return float(inp)/180.0


def birth_format(inp):
    return float(inp)/100.0
