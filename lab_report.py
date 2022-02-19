from math import sqrt
class lab_report:
    
    def __init__(self):
        pass
    
    def generate_simple_report(self, osc_list, physicist):
        '''creates single report or multiple based on how many experiments are to be done'''
        if physicist.number_of_experiments == 1:
            self.generate_single_frames_file(osc_list, physicist.frames_num[0], 0)
        elif physicist.number_of_experiments > 1 :
            self.generate_multiple_frames_files(osc_list, physicist.frames_num, physicist.number_of_experiments)
        if physicist.osc_num <= 4 :
            self.generate_single_frequencies_file(physicist)
        if physicist.osc_num > 100 :
            self.generate_single_v_wave_file(physicist)
    
    
    
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
        
    
    def generate_single_frequencies_file(self, physicist):
        scribe = open('frequencies.txt', 'a')
        for i in range(physicist.number_of_experiments):
            omega_analytic = str(physicist.omega) + '\t'
            scribe.write(omega_analytic)
            omega_approx = str(physicist.calculated_omega[i]) + '\t'
            scribe.write(omega_approx)
            delta_omega = abs(physicist.omega - physicist.calculated_omega[i])/physicist.omega
            delta_omega_str = str(delta_omega) + '\n'
            scribe.write(delta_omega_str)
            
        
    def generate_single_v_wave_file(self, physicist):
        scribe = open('v_wave.txt', 'a')
        v_wave_analytic = sqrt(physicist.k/physicist.mass)*physicist.L
        v_wave_analytic_str = str(v_wave_analytic) + '\t'
        for i in range(physicist.number_of_experiments):
            scribe.write(v_wave_analytic_str)
            v_wave_approx = str(physicist.calculated_wave_velocity[i]) + '\t'
            scribe.write(v_wave_approx)
            delta_v_wave = abs(v_wave_analytic - physicist.calculated_wave_velocity[i])/v_wave_analytic
            delta_omega_str = str(delta_v_wave) + '\n'
            scribe.write(delta_omega_str)
            
    
    
    
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