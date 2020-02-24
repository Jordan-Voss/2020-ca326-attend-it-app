from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty,ListProperty
from kivy.uix.floatlayout import FloatLayout
import pathlib
import csv
import mysql.connector

modules =[]

def add_mod_db(id,mod_name):
    print(id,mod_name)
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Attendit",
    database="attendit"
    )
    mycursor = mydb.cursor()

    query = "INSERT IGNORE INTO student (id, mod_name) VALUES (%s, %s)"
    for m in mod_name:
        val = (0,m)
        try:
            mycursor.execute(query, val)
            mydb.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
def add_details_db(mod,day,time,location):
    print(id,mod)
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Attendit",
    database="attendit"
    )
    mycursor = mydb.cursor()

    query = "UPDATE student SET day = %s, time = %s, location = %s  WHERE mod_name = %s ;"
    val = (day, time, location, mod)
    try:
        mycursor.execute(query,val)
        mydb.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        App.get_running_app().stop()

class LoginWindow(Screen):
    pass

class MainWindow(Screen):
    nam = ObjectProperty(None)
    #day = ObjectProperty(None)
    #time = ObjectProperty(None)
    #dur = ObjectProperty(None)
    loc = ObjectProperty(None)



#what to do when button pressed
    def pressed(self):
        global modules
        if self.nam.text != '':
            m_name = self.nam.text
            self.nam.text = ""
            if m_name not in modules:
                modules.append(m_name)
        print(modules)
    def pr(self):
        add_mod_db(1,modules)

class SecondWindow(Screen):

    def spinner_clicked(self,text):
        print(text)

    def mod_but_press(self,mod,day,time,loc):
        m_loc=self.loc.text
        self.loc.text=''
        print(mod,day,time,loc)
        add_details_db(mod,day,time,loc)

    def modules(self):
        print(modules)

    def __init__(self, **kwargs):
        self.buildLists()
        super(SecondWindow, self).__init__(**kwargs)

    def buildLists(self):
        self.pickType = ['Select',]
        self.pickSubType = ['Select']

    def updateSpinner(self, text):

        if text == 'Select':
            self.ids.spinner_1.values = modules


class WindowManager(ScreenManager):
    pass


#------------------------------------------------------------------------------#

kv = Builder.load_file("app.kv")


class MyMainApp(App):
    def build(self):

        return kv

#run the app
if __name__ == "__main__":
    MyMainApp().run()
