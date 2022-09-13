import csv

def get_blm_data(filename):
    data = []
    with open(filename) as f:
        for row in csv.DictReader(f):
            row_dict = {k: float(v) for k, v in row.items() if k != 'State'}
            row_dict['State'] = row['State']
            data.append(row_dict)
    return data

def get_diversity_data(filename):
    file_object = open(filename)
    rows = csv.DictReader(file_object, delimiter=',')
    data_dict = {}
    for row in rows:
        data_dict[row['Company']] = {k: float(v) for k, v in row.items() if k != 'Company'}
    return data_dict

def get_graduates_data(filename):
    data = []
    with open(filename) as f:
        for row in csv.DictReader(f):
            row_dict = {k: int(v) if k != 'Education.Major' else v for k, v in row.items()}
            data.append(row_dict)
    return data


def get_state_pops():
    return {'Alabama': 1359025,
            'Alaska': 382768,
            'Arizona': 4816902,
            'Arkansas': 816032,
            'California': 29044234,
            'Colorado': 3226330,
            'Connecticut': 1522919,
            'Delaware': 101276,
            'District of Columbia': 599620,
            'Florida': 9497148,
            'Georgia': 2423899,
            'Hawaii': 582887,
            'Idaho': 648635,
            'Illinois': 6289798,
            'Indiana': 2508905,
            'Iowa': 1057373,
            'Kansas': 1349359,
            'Kentucky': 1094053,
            'Louisiana': 1423072,
            'Maine': 129851,
            'Maryland': 2401948,
            'Massachusetts': 3199551,
            'Michigan': 3004677,
            'Minnesota': 2181353,
            'Mississippi': 510952,
            'Missouri': 1942357,
            'Montana': 295249,
            'Nebraska': 778507,
            'Nevada': 2234496,
            'New Hampshire': 232417,
            'New Jersey': 2110494,
            'New Mexico': 1040982,
            'New York': 10612671,
            'North Carolina': 3351401,
            'North Dakota': 262802,
            'Ohio': 3887738,
            'Oklahoma': 1662991,
            'Oregon': 1774109,
            'Pennsylvania': 2599981,
            'Rhode Island': 479649,
            'South Carolina': 743429,
            'South Dakota': 224005,
            'Tennessee': 2515486,
            'Texas': 14999365,
            'Utah': 1648183,
            'Vermont': 35859,
            'Virginia': 3021985,
            'Washington': 3180145,
            'West Virginia': 125905,
            'Wisconsin': 2033230,
            'Wyoming': 147609}
