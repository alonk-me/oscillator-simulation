
class physicist:
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
        return  acceleration    # can be changed to ososcillator.a without return 
        
    def calculate_force_on_n_oscillator(self, oscillator_list, n):
        n__minus_n_minus_one = (oscillator_list[n].get_delta_x(self.L)) - (oscillator_list[n-1].get_delta_x(self.L))
        n__minus_n_plus_one = (oscillator_list[n].get_delta_x(self.L)) - (oscillator_list[n+1].get_delta_x(self.L))
        return (-1)*self.k*(n__minus_n_minus_one) - (self.k*n__minus_n_plus_one) 
    
    def calculate_force_on_n_first_oscillator(self, oscillator_list, n):
        n__minus_n_plus_one = (oscillator_list[n].get_delta_x(self.L)) - (oscillator_list[n+1].get_delta_x(self.L))
        return (-1)*self.k*(n__minus_n_plus_one)
    
    def calculate_force_on_n_last_oscillator(self, oscillator_list, n):
        n_minus_n_minus_one = (oscillator_list[n].get_delta_x(self.L)) - (oscillator_list[n-1].get_delta_x(self.L))
        return (-1)*self.k*(n_minus_n_minus_one)
        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def calculate_coordinate_single_oscillator(self, oscillator, delta_time):
        coordinate = oscillator.x + delta_time*oscillator.v
        return coordinate
    
    def calculate_velocity_single_oscillator_n_plus_one_step(self, oscillator, delta_time):
        velocity = oscillator.v + delta_time*oscillator.a
        return velocity
    
    def calculate_velocity_single_oscillator_step_one(self, oscillator, delta_time):
        velocity = oscillator.v + 0.5*delta_time*oscillator.a
        return velocity
       
    def calculate_acceleration_single_oscillator(self, oscillator):
        if oscillator.static == True:
            return 0
        force = self.calculate_force_on_single_oscillator(oscillator.x)
        acceleration = force/self.mass
        return  acceleration    # can be changed to oscillator.a without return 
        
    def calculate_force_on_single_oscillator(self, x):
        return (-1)*(2*self.k*(x-self.L))    
    