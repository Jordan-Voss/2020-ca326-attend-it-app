import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

#module class to store module attributes
class Module():
    def __init__(self,name,day,time,duration,location):
        self.name = name
        self.day = day
        self.time = time
        self.dur = duration
        self.loc = location
    def show(mod):
        return mod.name,mod.day,mod.time,mod.dur,mod.loc

#create kivy grid to place text boxes,buttons etc.
class ModuleGrid(Widget):
    name = ObjectProperty(None)
    day = ObjectProperty(None)
    time = ObjectProperty(None)
    dur = ObjectProperty(None)
    loc = ObjectProperty(None)
    #what to do when button pressed
    def pressed(self):
        m_name = self.name.text
        self.name.text = ""
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
        mod = Module(m_name,m_day,m_time,m_duration,m_location)
        print(mod.show(), mod.time)
        

class TimetableApp(App):
    def build(self):
        return ModuleGrid()
#class GenttButton(App):
#    def build(self):
#        but = Button()
#        return but
#    def on_press_button(self):
#        print("pressed")

if __name__ == '__main__':
    TimetableApp().run()
