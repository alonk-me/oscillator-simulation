class oscillator:
    def __init__(self, x_init, v_init, osc_index, static=False, last=False):
        self.x = x_init
        self.v = v_init
        self.osc_index = osc_index
        self.static = static
        self.last = last
        self.a = 0
        self.coordinates_data = []
        self.velocity_data = []
        
    def update_x(self, new_x):
        self.coordinates_data.append(self.x)
        self.x = new_x
   
    def update_v(self, new_v):
        self.velocity_data.append(self.v)
        self.v = new_v
            
            
    def get_delta_x(self, L):
        return self.x - (L*self.osc_index)