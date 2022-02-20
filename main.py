import file_parser
from physicist import *
from lab_report import *
'''main file to load and initiate program '''

input_file_path = input('please insert full path to init state json file:')
params_file_path = input('please insert full path to parameters json file:')

input_data = file_parser.json_file_parser(input_file_path)   
parameters_data = file_parser.json_file_parser(params_file_path)

einstein = physicist(parameters_data, input_data)
osc_list = []
einstein.initate_oscillators(osc_list)
einstein.run_experiment(osc_list)


report = lab_report()
report.generate_simple_report(osc_list, einstein)

