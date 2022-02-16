import file_parser
from physicist import *
from oscillator import *

input_file_path = '/example/input_initState4.json'   # can be changed to cmd read
params_file_path = '/example/input_parameters4.json'  # can be changed to cmd read

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
    for frame in range(1):
    # for frame in range(einstein.frames_num[j]):
        for i in range(len(osc_list)):
            osc_list[i].a = einstein.calculate_acceleration_n_oscillators(osc_list, i)
            new_v = 0
            if frame == 0 :
                new_v = einstein.calculate_oscillator_velocity_step_one(osc_list[i], einstein.dt[j])   # dt needs to be looped with frames, and add if statment for first step
            elif frame != 0 :
                new_v = einstein.calculate_oscillator_velocity_n_plus_one_step(osc_list[i], einstein.dt[j])
            osc_list[i].update_v(new_v)
            new_x = einstein.calculate_oscillator_coordinate(osc_list[i], einstein.dt[j])
            osc_list[i].update_x(new_x)
            print('new x:' , osc_list[i].x)
