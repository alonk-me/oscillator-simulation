import json
import os

def json_file_parser(j):
    file_path = os.path.dirname(__file__) + j
    with open(file_path, 'r') as input_file:
        input_data = json.load(input_file)
    return input_data
''' function to load json file as dictionary  '''
 
# def param_file_parser(j):
#     file_path = os.path.dirname(__file__) + j
#     with open(file_path, 'r') as input_file:
#         param_data = json.load(input_file)
#     return param_data


