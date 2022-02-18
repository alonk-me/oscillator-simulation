class lab_report:
    def __init__(self):
        pass
    
    def generate_simple_report(self, osc_list, physicist):
        '''creates single report or multiple based on how many experiments are to be done'''
        if physicist.number_of_experiments == 1:
            self.generate_single_frames_file(osc_list, physicist.frames_num[0], 0)
        elif physicist.number_of_experiments > 1 :
            self.generate_multiple_frames_files(osc_list, physicist.frames_num, physicist.number_of_experiments)
    
    
    
    def generate_multiple_frames_files(self, osc_list, num_frames, number_of_experiments):
        ''' generate multiple frames file. sometimes tab looks like space, depends on text editor. '''
        for experiment in range(number_of_experiments):
            scribe = open(f'frames{experiment+1}.txt', 'a')
            for i in range(num_frames[experiment]):
                for j in range(len(osc_list)):
                    if osc_list[j].last:
                        value = str(osc_list[j].coordinates_data[experiment][i])
                    else:
                        value = str(osc_list[j].coordinates_data[experiment][i]) + '\t'
                    scribe.write(value)
                
                scribe.write('\n')
            scribe.close()
    
    
    def generate_single_frames_file(self, osc_list, num_frames, experiment_number):
        ''' generate single frames file. sometimes tab looks like space, depends on text editor. '''
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