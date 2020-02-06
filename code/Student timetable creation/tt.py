**********import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
modules = []

class ModuleGrid(GridLayout):
    def __init__(self,**kwargs):
        super(ModuleGrid,self).__init__(**kwargs)
        self.inside = GridLayout()
        self.inside.cols = 3
        self.cols = 1
        self.inside.orientation = 'vertical'

        self.inside.add_widget(Label(text="Module Name: ",size_hint = (.5, .25)))
        self.name = TextInput(multiline=False,size_hint = (.5, 1))
        self.inside.add_widget(self.name)
        self.inside.add_widget(Label(size_hint = (.5, .25)))

        self.inside.add_widget(Label(text="Module Start Time: ",size_hint = (.5, .25)))
        self.time = TextInput(multiline=False,size_hint = (.5, 1))
        self.inside.add_widget(self.time)
        self.inside.add_widget(Label(size_hint = (.5, .25)))

        self.inside.add_widget(Label(text="Module Duration: ",size_hint = (.5, .25)))
        self.dur = TextInput(multiline=False,size_hint = (.5, 1))
        self.inside.add_widget(self.dur)
        self.inside.add_widget(Label(size_hint = (.5, .25)))

        self.inside.add_widget(Label(text="Module Location: ",size_hint = (.5, .25)))
        self.loc = TextInput(multiline=False,size_hint = (.5, 1))
        self.inside.add_widget(self.loc)
        self.inside.add_widget(Label(size_hint = (.5, .25)))

        self.add_widget(self.inside)

        self.inside.add_widget(Label(size_hint = (1, 1.5)))
        self.submit_module = Button(text="Add Module", size_hint = (1,.5),
        pos_hint = {'center_x': .5, 'center_y':.5})
        self.submit_module.bind(on_press=self.pressed)
        self.inside.add_widget(self.submit_module)
        self.inside.add_widget(Label(size_hint = (1, 1.5)))


        self.add_widget(Label(size_hint = (1, 1)))
    def pressed(self,instance):
        m_name = self.name.text
        self.name.text = ""
        m_time = self.time.text
        self.time.text = ""
        m_duration = self.dur.text
        self.dur.text = ""
        m_location = self.loc.text
        self.loc.text = ""
        modules.append(m_name)
        modules.append(m_time)
        modules.append(m_duration)
        modules.append(m_location)
        print(modules)



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
