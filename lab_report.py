from matplotlib import pyplot
from matplotlib import style
from math import sqrt
class lab_report:
    
    def __init__(self):
        '''a class to generate all plots and text files '''
        pass
    
    def generate_simple_report(self, osc_list, physicist):
        '''initiates report processing, single report or multiple based on how many experiments are to be done'''
        if physicist.number_of_experiments == 1:
            self.generate_single_frames_file(osc_list, physicist.frames_num[0], 0)
        elif physicist.number_of_experiments > 1 :
            self.generate_multiple_frames_files(osc_list, physicist.frames_num, physicist.number_of_experiments)
        if physicist.osc_num <= 4 :
            self.generate_single_frequencies_file(physicist)
        if physicist.osc_num > 100 :
            self.generate_single_v_wave_file(physicist)
        self.generate_plots(physicist, osc_list)
    
    
    
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
        '''generates a  frequencies text file'''
        delta_omega_list = []
        scribe = open('frequencies.txt', 'a')
        for i in range(physicist.number_of_experiments):
            omega_analytic = str(physicist.omega) + '\t'
            scribe.write(omega_analytic)
            omega_approx = str(physicist.calculated_omega[i]) + '\t'
            scribe.write(omega_approx)
            delta_omega = abs(physicist.omega - physicist.calculated_omega[i])/physicist.omega
            delta_omega_list.append(delta_omega)
            delta_omega_str = str(delta_omega) + '\n'
            scribe.write(delta_omega_str)
            
        if physicist.osc_num == 3 :
            self.generate_omega_plot(physicist, delta_omega_list)
            
        
    def generate_single_v_wave_file(self, physicist):
        '''generates a  v_wave text file'''
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
            

        
    def generate_plots(self, physicist, osc_list):
        '''initiates plotting '''
        for experiment in range(physicist.number_of_experiments):
            time_list = []
            for i in range(physicist.frames_num[experiment]):
                time_list.append(i*physicist.dt[experiment])
    
            self.generate_energy_plots(physicist, experiment, time_list)
            self.generate_motion_plots(physicist, osc_list, experiment, time_list)
            
       
    
       
        
        
    def generate_motion_plots(self, physicist, osc_list, experiment, time_list):
        '''plots motion graphs: acceleration, velocity, delta x '''
        middle_index = len(osc_list)//2
        delta_x = []
        for coordinate in osc_list[middle_index].coordinates_data[experiment]:
            delta_x.append(coordinate - (middle_index*physicist.L))
        pyplot.style.use('seaborn-darkgrid')
        fig, (ax1, ax2, ax3) = pyplot.subplots(3)
        ax1.plot(time_list, delta_x, label='delta x', color='g')   
        ax2.plot(time_list, osc_list[middle_index].velocity_data[experiment], label='velocity', color='r')
        ax3.plot(time_list, osc_list[middle_index].acceleration_data[experiment], label='acceleration', color='b')
        ax1.legend()
        ax1.set_title(f'delta x as a function of time for experiment {experiment+1}')
        ax1.set_xlabel('time (s)')
        ax1.set_ylabel('location (m)')
        ax2.legend()
        ax2.set_title(f'velocity as a function of time for experiment {experiment+1}')
        ax2.set_xlabel('time (s)')
        ax2.set_ylabel('velocity (m/s)')
        ax3.legend()
        ax3.set_title(f'acceleration as a function of time for experiment {experiment+1}')
        ax3.set_xlabel('time (s)')
        ax3.set_ylabel('acceleration (m/s^2)')
        pyplot.tight_layout()
        if physicist.number_of_experiments == 1:
            fig.savefig(f'kinematics.png')
        if physicist.number_of_experiments > 1:
            fig.savefig(f'kinematics{experiment+1}.png')
        pyplot.close
        


    def generate_energy_plots(self, physicist, experiment, time_list):
        ''' plots energy graphs'''
        pyplot.style.use('seaborn-darkgrid')
        
        fig, (ax1, ax2, ax3, ax4) = pyplot.subplots(4)
        ax1.plot(time_list, physicist.kinetic_energy[experiment], color='g')
        ax1.set_title('kinetic energy')
        ax1.set_xlabel('time (s)')
        ax1.set_ylabel('energy (joule)')

        ax2.plot(time_list, physicist.potential_energy[experiment], color='r')
        ax2.set_title('potential energy')
        ax2.set_xlabel('time (s)')
        ax2.set_ylabel('energy (joule)')
        

        ax3.plot(time_list, physicist.total_energy[experiment], color='b')
        ax3.set_title('total energy')
        ax3.set_xlabel('time (s)')
        ax3.set_ylabel('energy (joule)')

        ax4.plot(time_list, physicist.kinetic_energy[experiment], color='r')
        ax4.plot(time_list, physicist.potential_energy[experiment], color='r')
        ax4.plot(time_list, physicist.total_energy[experiment], color='b')
        
        ax4.set_title(f'combined graph energies')
        ax4.set_xlabel('time (s)')
        ax4.set_ylabel('energy (joule)')
        # fig.legend()
        pyplot.tight_layout()
        if physicist.number_of_experiments == 1:
            pyplot.savefig(f'Energy.png')
        if physicist.number_of_experiments > 1:
            pyplot.savefig(f'Energy{experiment+1}.png')
        pyplot.close('all')


        
    def generate_omega_plot(self, physicist, omega_delta_list):   
        '''graphs omega plot '''
        pyplot.style.use('seaborn-darkgrid')
        fig, ax = pyplot.subplots()
        ax.plot(physicist.dt, omega_delta_list, color='g')
        ax.legend()
        ax.set_title(f'delta omega as a function of delta time')
        ax.set_xlabel('delta time (s)')
        ax.set_ylabel('delta omega (hertz)')
        pyplot.tight_layout()
        fig.savefig('freq_vs_dt.png')
        pyplot.close(fig)     
