class oscillator:                                         
    def __init__(self, x_init, v_init, osc_index, static=False, last=False):
        self.x = x_init
        self.x_zero = x_init
        self.v = v_init
        self.v_zero = v_init
        self.osc_index = osc_index
        self.static = static
        self.last = last
        self.a = 0
        self.coordinates_data = [[]]
        self.velocity_data = [[]]
        self.experiment_number = 0
        
    def update_x(self, new_x):
        self.coordinates_data[self.experiment_number].append(self.x)
        self.x = new_x
   
    def update_v(self, new_v):
        self.velocity_data[self.experiment_number].append(self.v)
        self.v = new_v

    def get_delta_x(self, L):  
        return self.x - (L*self.osc_index)
        
    def refresh_oscillator_for_new_experiment(self):
        self.a = 0
        self.x = self.x_zero
        self.v = self.v_zero
        self.coordinates_data.append([])
        self.velocity_data.append([])
        self.experiment_number += 1
        
   
'''

oscillator is a class to hold the data that is specific to an individual oscillator. its functions are also individual and helps simplify the code 
update_v and update_x are both methods used to update data on an individual oscillator without deleting previous data 
get delta x returns the delta x for a specific oscillator 
refresh oscillator for new experiment puts the oscillator in a state ready for next dt cycle 

'''