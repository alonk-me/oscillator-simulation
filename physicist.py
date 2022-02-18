from oscillator import *

class physicist:
    '''physicist is a class to manage the experiment. it does this by calculating acceleration, force, velocity, coordinates for the particles . it takes in all the general data that is not specific to one oscillator.'''
    
    def __init__(self, params_list, input_list):
        self.mass = params_list['mass'] 
        self.k = params_list['k']
        self.x_list = input_list['x']
        self.v_list = input_list['v']
        self.L = params_list['l_rest']
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
        for i in range(self.osc_num):   # can incapsulate in physicist, under an initiate oscillators function
            if i == 0:
                osc_list.append(oscillator(self.x_list[i], self.v_list[i], i, not self.first_is_open))
            elif i+1 == self.osc_num:
                osc_list.append(oscillator(self.x_list[i], self.v_list[i], i, not self.last_is_open, True))
            else:    
                osc_list.append(oscillator(self.x_list[i], self.v_list[i], i,))
    
        
       
      
    def run_experiment(self, osc_list):
        for j in range(self.number_of_experiments):    
            for frame in range(self.frames_num[j]): 
                self.measure_and_document_acceleration(osc_list)
                self.measure_and_document_velocity(osc_list, frame, j)
                self.measure_and_document_coordinate(osc_list, frame, j)
            self.reset_experiment(osc_list)
            
    def measure_and_document_acceleration(self, osc_list):
        for i in range(len(osc_list)):
            osc_list[i].a = self.calculate_acceleration_n_oscillators(osc_list, i)
      
    def measure_and_document_velocity(self, osc_list, frame, j):  
        for s in range(len(osc_list)):
            new_v = 0
            if frame == 0 :
                new_v = self.calculate_oscillator_velocity_step_one(osc_list[s], self.dt[j])   
            elif frame != 0 :
                new_v = self.calculate_oscillator_velocity_n_plus_one_step(osc_list[s], self.dt[j])
            osc_list[s].update_v(new_v)
    
    def measure_and_document_coordinate(self, osc_list, frame, j):   
        for l in range(len(osc_list)):  
            new_x = 0
            new_x = self.calculate_oscillator_coordinate(osc_list[l], self.dt[j])
            osc_list[l].update_x(new_x)
            
    

            
    def reset_experiment(self, osc_list):
        ''' initiates a restart to oscillators'''
        for k in range(self.osc_num):   
            osc_list[k].refresh_oscillator_for_new_experiment()
    
    
