import json
import os

def json_file_parser(path):
    ''' function to load json file as dictionary  '''
    with open(path, 'r') as input_file:
        input_data = json.load(input_file)
    return input_data

 
