class oscillator:
    '''oscillator is a class to hold the data that is specific to an individual oscillator. its functions are also individual and helps simplify the code  '''
    def __init__(self, x_init, v_init, osc_index, static=False, last=False):
        ''' oscillator data '''
        self.x = x_init
        self.x_zero = x_init
        self.v = v_init
        self.v_zero = v_init
        self.osc_index = osc_index
        self.static = static
        self.last = last
        self.a = 0
        self.acceleration_data = [[]]
        self.coordinates_data = [[]]
        self.velocity_data = [[]]
        self.experiment_number = 0
        self.time_regression_velocity_data = [[]]
        
    def update_x(self, new_x):
        '''method used to update location data on an individual oscillator without deleting previous data  '''
        self.coordinates_data[self.experiment_number].append(self.x)
        self.x = new_x
   
    def update_v(self, new_v):
        '''method used to update velocity data on an individual oscillator without deleting previous data  '''
        self.velocity_data[self.experiment_number].append(self.v)
        self.v = new_v

    def update_a(self, new_a):
        '''method used to update acceleration data on an individual oscillator without deleting previous data  '''
        self.acceleration_data[self.experiment_number].append(self.a)
        self.a = new_a


    def get_delta_x(self, L):
        '''function to calculate delta x of individual oscillator '''
        return self.x - (L*self.osc_index)
        
    def refresh_oscillator_for_new_experiment(self):  
        '''method to restore oscillator to factory settings before next experiment(new dt/frames) '''
        self.a = 0
        self.x = self.x_zero
        self.v = self.v_zero
        self.acceleration_data.append([])
        self.coordinates_data.append([])
        self.velocity_data.append([])
        self.experiment_number += 1
        
   

                