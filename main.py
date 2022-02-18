import file_parser
from physicist import *
from lab_report import *


input_file_path = '/example/input_initState3.json'   # can be changed to cmd read
params_file_path = '/example/input_parameters3.json'  # can be changed to cmd read

input_data = file_parser.json_file_parser(input_file_path)   
parameters_data = file_parser.json_file_parser(params_file_path)
einstein = physicist(parameters_data, input_data)
osc_list = []
einstein.initate_oscillators(osc_list)
print(osc_list)


# for i in range(einstein.osc_num):   # can incapsulate in physicist, under an initiate oscillators function
#     if i == 0:
#         osc_list.append(oscillator(einstein.x_list[i], einstein.v_list[i], i, not einstein.first_is_open))
#     elif i+1 == einstein.osc_num:
#         osc_list.append(oscillator(einstein.x_list[i], einstein.v_list[i], i, not einstein.last_is_open, True))
#     else:    
#         osc_list.append(oscillator(einstein.x_list[i], einstein.v_list[i], i,))

einstein.run_experiment(osc_list)

report = lab_report()
report.generate_simple_report(osc_list, einstein)

