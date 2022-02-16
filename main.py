import file_parser
from physicist import *
from oscillator import *

input_file_path = '/example/input_initState4.json'
params_file_path = '/example/input_parameters4.json'

input_data = file_parser.json_file_parser(input_file_path)
parameters_data = file_parser.json_file_parser(params_file_path)
einstein = physicist(parameters_data, input_data)
osc_list = []

for i in range(einstein.osc_num):
    if i == 0:
        osc_list.append(oscillator(einstein.x_list[i], einstein.v_list[i], i, not einstein.first_is_open))
    elif i+1 == einstein.osc_num:
        osc_list.append(oscillator(einstein.x_list[i], einstein.v_list[i], i, not einstein.last_is_open, True))
    else:    
        osc_list.append(oscillator(einstein.x_list[i], einstein.v_list[i], i,))

for j in range(einstein.number_of_experiments):
    for frame in range(einstein.frames_num[j])
        for i in range(len(osc_list)):
            # print('old x:' , osc_list[i].x)
            osc_list[i].a = einstein.calculate_acceleration_n_oscillators(osc_list, i)
            new_v = einstein.calculate_velocity_single_oscillator_step_one(osc_list[i], einstein.dt[0])   # dt needs to be looped with frames, and add if statment for first step
            # print('new v:', new_v)
            osc_list[i].update_v(new_v)
            new_x = einstein.calculate_coordinate_single_oscillator(osc_list[i], einstein.dt[0])
            osc_list[i].update_x(new_x)
            print('new x:' , osc_list[i].x)
