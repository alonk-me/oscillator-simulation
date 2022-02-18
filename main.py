import file_parser
from physicist import *
from lab_report import *


input_file_path = '/example/input_initState1.json'   # can be changed to cmd read
params_file_path = '/example/input_parameters1.json'  # can be changed to cmd read

input_data = file_parser.json_file_parser(input_file_path)   
parameters_data = file_parser.json_file_parser(params_file_path)

einstein = physicist(parameters_data, input_data)
osc_list = []
einstein.initate_oscillators(osc_list)
einstein.run_experiment(osc_list)

print(einstein.kinetic_energy)
print(einstein.potential_energy)
print(einstein.total_energy)
report = lab_report()
report.generate_simple_report(osc_list, einstein)

