import json
import os

def json_file_parser(j):
    ''' function to load json file as dictionary  '''
    file_path = os.path.dirname(__file__) + j
    print(file_path)
    with open(file_path, 'r') as input_file:
        input_data = json.load(input_file)
    return input_data

 
