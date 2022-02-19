import file_parser
from physicist import *
from lab_report import *


input_file_path = '/example/input_initState4.json'   # can be changed to cmd read
params_file_path = '/example/input_parameters4.json'  # can be changed to cmd read

input_data = file_parser.json_file_parser(input_file_path)   
parameters_data = file_parser.json_file_parser(params_file_path)

einstein = physicist(parameters_data, input_data)
osc_list = []
einstein.initate_oscillators(osc_list)
einstein.run_experiment(osc_list)


report = lab_report()
report.generate_simple_report(osc_list, einstein)

