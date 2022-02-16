class lab_report:
    def __init__(self):
        pass
    
    def generate_simple_report(self):
        pass
    
    def generate_frames_file(self, osc_list, num_frames, experiment_number):
        ''' sometimes tab looks like space, depends on text editor. '''
        scribe = open('frames.txt', 'a')
        for i in range(num_frames):
            for j in range(len(osc_list)):
                if osc_list[j].last:
                    value = str(osc_list[j].coordinates_data[experiment_number][i])
                else:
                    value = str(osc_list[j].coordinates_data[experiment_number][i]) + '\t'
                scribe.write(value)
                
            scribe.write('\n')
        scribe.close()
        
    def generate_velocity_file(self, osc_list, num_frames, experiment_number):
        ''' sometimes tab looks like space, depends on text editor. '''
        scribe = open('velocity.txt', 'a')
        for i in range(num_frames):
            for j in range(len(osc_list)):
                if osc_list[j].last:
                    value = str(osc_list[j].velocity_data[experiment_number][i])
                else:
                    value = str(osc_list[j].velocity_data[experiment_number][i]) + '\t'
                scribe.write(value)
                
            scribe.write('\n')
        scribe.close()
        
        
    def generate_html_report(self, osc_list, num_frames):
        pass