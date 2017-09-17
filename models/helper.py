import numpy as np


def count_chars(inp):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lowercase = inp.lower()
    dict = {}
    for a in alphabet:
        dict[a] = 0
    for char in lowercase:
        if 'a' <= char <= 'z':
            dict[char] += 1
    res = []
    for char in alphabet:
        res.append(dict[char])
    return res


def parse_query(name, sex, lat, long, birth, product, coverage, premium, plan):
    name = count_chars(name)
    sex = sex_format(sex)
    lat = lat_long_format(lat)
    long = lat_long_format(long)
    birth = birth_format(birth)
    product = product_format(product)
    coverage = coverage_format(coverage)
    premium = premium_format(premium)
    plan = plan_format(plan)
    curr_inp = name + sex + lat + long + birth + product + coverage + premium + plan
    return np.asarray(curr_inp)

def read_data(filename):
    input_x = []
    output = []

    with open(filename, 'r') as csv_file:
        for row in csv_file:
            temp = row.split(',')
            if temp.__len__() != 12:
                continue
            name = count_chars(temp[0])
            sex = sex_format(temp[1])
            lat = lat_long_format(temp[2])
            long = lat_long_format(temp[3])
            birth = birth_format(temp[4])
            product = product_format(temp[5])
            coverage = coverage_format(temp[6])
            premium = premium_format(temp[7])
            plan = plan_format(temp[8])
            curr_inp = name + sex + lat + long + birth + product + coverage + premium + plan
            input_x.append(np.asarray(curr_inp))
            msg_id = temp[9]
            method = temp[10]
            output.append(output_format(msg_id, method))
    return np.asarray(input_x), np.asarray(output)


def sex_format(inp):
    if inp == 'M':
        return [1, 0]
    else:  # if sex is F
        return [0, 1]


def lat_long_format(inp):
    res = [float(inp) / 180.0]
    return res


def birth_format(inp):
    res = [float(inp) / 100.0]
    return res


def product_format(inp):
    if inp == 'dental':
        return [1, 0]
    else:  # if coverage is accidental
        return [0, 1]


def coverage_format(inp):
    if inp == 'family':
        return [1, 0]
    else:  # if coverage is private
        return [0, 1]


def premium_format(inp):
    if inp == 18:
        return [1, 0, 0, 0, 0, 0]
    if inp == 8:
        return [0, 1, 0, 0, 0, 0]
    if inp == 23:
        return [0, 0, 1, 0, 0, 0]
    if inp == 13:
        return [0, 0, 0, 1, 0, 0]
    if inp == 10:
        return [0, 0, 0, 0, 1, 0]
    else:  # if premium is 5
        return [0, 0, 0, 0, 0, 1]


def plan_format(inp):
    if inp == 'Silver':
        return [1, 0, 0]
    if inp == 'Gold':
        return [0, 1, 0]
    else:  # if plan is Regular
        return [0, 0, 1]


def output_format(msg_id, method):
    msg_id = int(msg_id)
    msg_id -= 1
    buffer = 0
    if method == 'Mail Flyer':
        buffer = 0
    elif method == 'Email':
        buffer = 1
    elif method == 'Letter':
        buffer = 2
    elif method == 'Call':
        buffer = 3
    elif method == 'Mail':
        buffer = 4
    index = msg_id * 5 + buffer
    res = np.zeros(55)
    res[index] = 1
    return np.asarray(res)
