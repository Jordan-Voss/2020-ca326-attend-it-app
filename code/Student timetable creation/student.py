from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import pathlib
import csv

class MainWindow(Screen):
    nam = ObjectProperty(None)
    day = ObjectProperty(None)
    time = ObjectProperty(None)
    dur = ObjectProperty(None)
    loc = ObjectProperty(None)



#what to do when button pressed
    def pressed(self):
        global avail_days
        global modules
        m_name = self.nam.text
        self.nam.text = ""
        m_day = self.day.text
        self.day.text = ""
        m_time = self.time.text
        self.time.text = ""
        m_duration = self.dur.text
        self.dur.text = ""
        m_location = self.loc.text
        self.loc.text = ""
    #modules.append(m_name)
    #modules.append(m_time)
    ##modules.append(m_duration)
    #modules.append(m_location)
    #print(modules)
        modules.append(m_name)

        print(modules)
    def next(self):
        m_name = self.nam.text
        self.nam.text = ""
        m_day = self.day.text
        self.day.text = ""
        m_time = self.time.text
        self.time.text = ""
        m_duration = self.dur.text
        self.dur.text = ""
        m_location = self.loc.text
        self.loc.text = ""


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


#------------------------------------------------------------------------------#
#Code for creating timetable to be introduced to second window
modules = []
modules_loc = {'.':'Nothing Scheduled'}
start_time = 6 #time starts at 6am
next_time = 7
avail_days = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
]
time_slot_list = []
module_per_slot = {} #dictionary for writing to csv
mod_at_time=[]
def fill_out_modules():

    #modules = input('type module - location , \n') #Take all module names
    #split them in order to be able to determine separate values
    all_modules = modules.replace(', ', ',')
    all_modules = modules.replace('- ', '-')
    all_modules = modules.replace(' -', '-')
#	all_modules = modules.replace('. ', '.')
#	all_modules = modules.replace(' .', '.')
    #split modules
    all_modules = all_modules.split(',')
    for mod in all_modules:
        #split module and location
        m = mod.split('-')
        modules_loc[m[0]] = m[1]

    return modules_loc
#function to ask what needs to be put at each time
def ask_time():
    print(f'modules list: {modules_loc}')
    print(f'Planning time: {start_time}h-{next_time}h')
    user_answer = input('What module do you want put here? Enter "."" for nothing')
    return user_answer
#function to create the timetable in a csv file
def create_table():
    tt_path = pathlib.Path.cwd() / 'My_Timetable.csv'

    with open(tt_path,'w') as tt_file:
        write_tt = csv.writer(tt_file)

        head = ['Time']
        head.extend(avail_days)
        write_tt.writerow(head)
        print(head)
        for hour, mod in module_per_slot.items():
            timeline = [hour]
            i =0
            while i < len(mod):
                if mod[i] == '.':
                    mod[i] = 'Nothing Scheduled'
                i += 1
            line = timeline + mod
            write_tt.writerow(line)
            print(line)

#------------------------------------------------------------------------------#

#allows the .kv file to be named anything we like
kv = Builder.load_file("student.kv")


class MyMainApp(App):
    def build(self):
        return kv

#run the app
if __name__ == "__main__":
    MyMainApp().run()
