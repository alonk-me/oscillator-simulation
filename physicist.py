from oscillator import *
import scipy.signal

class physicist:
    '''physicist is a class to manage the experiment. it does this by calculating acceleration, force, velocity, coordinates for the particles . it takes in all the general data that is not specific to one oscillator.'''
    
    def __init__(self, params_list, input_list):
        self.mass = params_list['mass'] 
        self.k = params_list['k']
        self.x_list = input_list['x']
        self.v_list = input_list['v']
        self.L = params_list['l_rest']
        self.kinetic_energy = []
        self.potential_energy = []
        self.total_energy = []
        self.first_is_open = params_list['first_is_open']
        self.last_is_open = params_list['last_is_open']
        self.osc_num = params_list['osc_num']
        self.omega = params_list['omega']
        self.frames_num = params_list['frames_num']
        self.dt = params_list['dt']
        self.number_of_experiments = len(params_list['dt'])
    
    
    def calculate_acceleration_n_oscillators(self, oscillator_list, n):
        ''' calculates the acceleration on an n two sided oscillator, or first one sided, or last one sided'''
        force = 0
        if oscillator_list[n].static == True:
            return 0
        elif oscillator_list[n].last:
            force = self.calculate_force_on_n_last_oscillator(oscillator_list, n)
        elif n == 0:
            force = self.calculate_force_on_n_first_oscillator(oscillator_list, n)
        else:
            force = self.calculate_force_on_n_oscillator(oscillator_list, n)
        acceleration = force/self.mass
        return  acceleration    
        
    def calculate_force_on_n_oscillator(self, oscillator_list, n):
        ''' calculates the force on a n oscillator'''
        n__minus_n_minus_one = (oscillator_list[n].get_delta_x(self.L)) - (oscillator_list[n-1].get_delta_x(self.L))
        n__minus_n_plus_one = (oscillator_list[n].get_delta_x(self.L)) - (oscillator_list[n+1].get_delta_x(self.L))
        return (-1)*self.k*(n__minus_n_minus_one) - (self.k*n__minus_n_plus_one) 
    
    def calculate_force_on_n_first_oscillator(self, oscillator_list, n):
        ''' calculates the force on a first oscillator in chain'''
        n__minus_n_plus_one = (oscillator_list[n].get_delta_x(self.L)) - (oscillator_list[n+1].get_delta_x(self.L))
        return (-1)*self.k*(n__minus_n_plus_one)
    
    def calculate_force_on_n_last_oscillator(self, oscillator_list, n):
        ''' calculates the force on a last oscillator in chain'''
        n_minus_n_minus_one = (oscillator_list[n].get_delta_x(self.L)) - (oscillator_list[n-1].get_delta_x(self.L))
        return (-1)*self.k*(n_minus_n_minus_one)
        
    
    
    def calculate_oscillator_coordinate(self, oscillator, delta_time):
        ''' calculates the coordinate of a single oscillator '''
        coordinate = oscillator.x + delta_time*oscillator.v
        return coordinate
    
    def calculate_oscillator_velocity_step_one(self, oscillator, delta_time):
        ''' calculates the velocity of a single oscillator for the first step'''
        velocity = oscillator.v + 0.5*delta_time*oscillator.a
        return velocity
        
    
    def calculate_oscillator_velocity_n_plus_one_step(self, oscillator, delta_time):
        ''' calculates the velocity of a single oscillator from the second step onward'''
        velocity = oscillator.v + delta_time*oscillator.a
        return velocity
    
       
    def calculate_acceleration_single_oscillator(self, oscillator):
        ''' calculates the acceleration of a single oscillator'''
        if oscillator.static == True:
            return 0
        force = self.calculate_force_on_single_oscillator(oscillator.x)
        acceleration = force/self.mass
        return  acceleration    # can be changed to oscillator.a without return 
        
    def calculate_force_on_single_oscillator(self, x):
        ''' calculates the force on a single oscillator'''
        return (-1)*(2*self.k*(x-self.L))    
       
       
       
       
    def initate_oscillators(self, osc_list):
        ''' a method to set all oscillators with their data'''
        for i in range(self.osc_num):   
            if i == 0:
                osc_list.append(oscillator(self.x_list[i], self.v_list[i], i, not self.first_is_open))
            elif i+1 == self.osc_num:
                osc_list.append(oscillator(self.x_list[i], self.v_list[i], i, not self.last_is_open, True))
            else:    
                osc_list.append(oscillator(self.x_list[i], self.v_list[i], i,))
    
        
       
      
    def run_experiment(self, osc_list):
        ''' a function to run the experiment loop'''
        for j in range(self.number_of_experiments):    
            for frame in range(self.frames_num[j]): 
                self.measure_and_document_acceleration(osc_list)
                self.measure_and_document_velocity(osc_list, frame, j)
                self.measure_and_document_coordinate(osc_list, frame, j)
            if j < (self.number_of_experiments - 1):
                self.reset_experiment(osc_list)
        self.run_post_experiment_analysis(osc_list)
            
    def measure_and_document_acceleration(self, osc_list):
        '''  measures acceleration of all oscillators in experiment '''
        for i in range(len(osc_list)):
            new_a = 0
            new_a = osc_list[i].a = self.calculate_acceleration_n_oscillators(osc_list, i)
            osc_list[i].update_a(new_a)
      
    def measure_and_document_velocity(self, osc_list, frame, j):  
        ''' measures and documents velocity of all oscillators in experiment'''
        for s in range(len(osc_list)):
            new_v = 0
            if frame == 0 :
                new_v = self.calculate_oscillator_velocity_step_one(osc_list[s], self.dt[j])   
            elif frame != 0 :
                new_v = self.calculate_oscillator_velocity_n_plus_one_step(osc_list[s], self.dt[j])
            osc_list[s].update_v(new_v)
    
    def measure_and_document_coordinate(self, osc_list, frame, j): 
        ''' measures and documents coordinate of all oscillators in experiment'''
        for l in range(len(osc_list)):  
            new_x = 0
            new_x = self.calculate_oscillator_coordinate(osc_list[l], self.dt[j])
            osc_list[l].update_x(new_x)
            
    

            
    def reset_experiment(self, osc_list):  
        ''' initiates a restart to oscillators to simulate next dt/frames '''
        for k in range(self.osc_num):   
            osc_list[k].refresh_oscillator_for_new_experiment()
    
    
    def run_post_experiment_analysis(self,osc_list):
        self.update_oscillators_with_time_regression(osc_list)
        self.calc_E(osc_list)
        # self.mean_frequency(osc_list, 0)
    
    
    
    def update_oscillators_with_time_regression(self, osc_list):
        for osc in osc_list:
            self.calculate_and_set_time_regression_velocity_array(osc)
    
    

    def calculate_and_set_time_regression_velocity_array(self, osc):
        for experiment in range(self.number_of_experiments):
            dt_experiment = self.dt[experiment]
            for i in range(len(osc.velocity_data[experiment])):
                if i == 0:
                    osc.time_regression_velocity_data[experiment].append(osc.v_zero)

                elif i > 1 :
                    velocity_i_plus_half = osc.velocity_data[experiment][i]
                    acceleration = osc.acceleration_data[experiment][i-1]
                    velocity_i = velocity_i_plus_half - (acceleration*dt_experiment*0.5)
                    osc.time_regression_velocity_data[experiment].append(velocity_i)
        
            velocity_i_minus_half = osc.velocity_data[experiment][-1]
            acceleration = osc.acceleration_data[experiment][-1]
            velocity_i = velocity_i_minus_half + (acceleration*dt_experiment*0.5)
            osc.time_regression_velocity_data[experiment].append(velocity_i)
            
            if experiment < (self.number_of_experiments - 1):
                osc.time_regression_velocity_data.append([])
        
        
    def calc_E(self, osc_list):
        for experiment in range(self.number_of_experiments):
            self.kinetic_energy.append(self.calculate_kinetic_energy(osc_list, experiment))
            self.potential_energy.append(self.calculate_potential_energy(osc_list, experiment))
            self.total_energy.append(self.calculate_total_energy(osc_list, experiment))

                
        
    def calculate_kinetic_energy(self, osc_list, experiment_number):
        kinetic_energy_in_experiment = []
        for frame in range(self.frames_num[experiment_number]):
            kinetic_energy_in_frame = 0
            for osc in osc_list:
                kinetic_energy_of_n_oscillator = 0.5*self.mass*(osc.time_regression_velocity_data[experiment_number][frame])**2
                kinetic_energy_in_frame += kinetic_energy_of_n_oscillator
            kinetic_energy_in_experiment.append(kinetic_energy_in_frame)
        return kinetic_energy_in_experiment
            
    def calculate_potential_energy(self,osc_list, experiment_number):
        potential_energy_in_experiment = []
        for frame in range(self.frames_num[experiment_number]):
            potential_energy_in_frame = 0
            for i in range(len(osc_list) - 2):
                delta_x_n_plus_one = (osc_list[i+1].coordinates_data[experiment_number][frame]) - (self.L*osc_list[i+1].osc_index)
                delta_x_n = (osc_list[i].coordinates_data[experiment_number][frame]) - (self.L*osc_list[i].osc_index)
                n_plus_one_minus_n =  - delta_x_n_plus_one - delta_x_n
                potential_energy_of_n_oscillator = 0.5*self.k*(n_plus_one_minus_n)**2
                potential_energy_in_frame += potential_energy_of_n_oscillator
            potential_energy_in_experiment.append(potential_energy_in_frame)
        return potential_energy_in_experiment

    def calculate_total_energy(self, osc_list, experiment_number):
        total_energy_in_experiment = []
        for frame in range(self.frames_num[experiment_number]):
            total_energy_in_frame = self.potential_energy[experiment_number][frame] + self.kinetic_energy[experiment_number][frame]
            total_energy_in_experiment.append(total_energy_in_frame) 
        return total_energy_in_experiment 

    def mean_frequency(self, osc_list, experiment_number):
        if self.osc_num != 3 and self.osc_num != 4:
            return null
        elif self.osc_num == 3:
            indices, x_peaks = scipy.signal.find_peaks(osc_list[1].coordinates_data[experiment_number], height=osc_list[1].coordinates_data[experiment_number][0])
            print('maxima indices are: ' , indices, 'x peaks are:', x_peaks)
            for peak in indices:
                print(f'peak should be: {osc_list[1].coordinates_data[experiment_number][peak]}' )
        
        
        # elif self.osc_num == 4:    
        #     for i in [2,3]
        #         find scipy.signal.find_peaks(osc_list[i].coordinates_data[experiment_number], height=osc_list[i].coordinates_data[experiment_number][0])
        # pass