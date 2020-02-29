from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty,ListProperty
from kivy.uix.floatlayout import FloatLayout
import mysql.connector
#------------------------------------------------------------------------------#
modules =[]
#function to add modules to database
#May no longer be needed as everythng will be added in the second function instead
# def add_mod_db(id,mod_name):
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="Attendit",
#     database="attendit"
#     )
#     mycursor = mydb.cursor()
#
#     query = "INSERT INTO student (id, mod_name) VALUES (%s, %s)"
#     for m in mod_name:
#         val = (0,m)
#         try:
#             mycursor.execute(query, val)
#             mydb.commit()
#         except mysql.connector.Error as err:
#             print("Something went wrong: {}".format(err))
#             App.get_running_app().stop()
#------------------------------------------------------------------------------#
#New function to add all details to database
#to make sure all instances of a module are recorded
#but not when there is a clash of times
def add_details_db(mod,day,time,location):
    #login details of the database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Attendit",
    database="attendit"
    )
    mycursor = mydb.cursor()
    query = "insert into student (id,mod_name,day,time,location) Select 0, %s,%s,%s,%s Where not exists(select * from student where mod_name=%s and day = %s and time = %s and location =%s)"
    values = (mod,day, time, location,mod,day,time,location)
    try:
        mycursor.execute(query,values)
        mydb.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        #exit app if error
        App.get_running_app().stop()
#------------------------------------------------------------------------------#
#Class for Login Screen
class LoginWindow(Screen):
    pass
#------------------------------------------------------------------------------#
class MainWindow(Screen):
#To get name and location from kivy file
    nam = ObjectProperty(None)
    loc = ObjectProperty(None)
#what to do when button pressed
    def pressed(self):
        global modules
        if self.nam.text != '':
            m_name = self.nam.text
            self.nam.text = ""
            if m_name not in modules:
                modules.append(m_name)

    def pr(self):
        global m
        m = modules[:]
#------------------------------------------------------------------------------#
#Class for original timetable creation
class SecondWindow(Screen):
    def spinner_clicked(self,text):
        print(text)
#add module location when button pressed
    def mod_but_press(self,mod,day,time,loc):
        m_loc=self.loc.text
        self.loc.text=''
#add to database
        add_details_db(mod,day,time,loc)
#Functions for updating spinners (dropdown menus)
    def __init__(self, **kwargs):
        self.buildLists()
        super(SecondWindow, self).__init__(**kwargs)

    def buildLists(self):
        self.pickType = ['Select',]
        self.pickSubType = ['Select']

    def updateSpinner(self, text):
        if text == 'Select':
            self.ids.spinner_1.values = modules
#------------------------------------------------------------------------------#
#Class for ranking modules page
class ThirdWindow(Screen):
#When button pressed make sure hours per week is between 0 and 41
    def prs(self):
        if self.hours.text.isdigit() and 0 < int(self.hours.text) <= 40:
            global s_hours,r_1,r_2,r_3,r_4,r_5,r_6
            s_hours = int(self.hours.text)
            r_1 = self.rnk_spin_1.text
            r_2 = self.rnk_spin_2.text
            r_3 = self.rnk_spin_3.text
            r_4 = self.rnk_spin_4.text
            r_5 = self.rnk_spin_5.text
            r_6 = self.rnk_spin_6.text
            self.manager.current = 'study'
        else:
            pass
        self.hours.text =''
#Updating spinners
    def __init__(self, **kwargs):
        self.buildLists2()
        m = modules[:]
        super(ThirdWindow, self).__init__(**kwargs)
    def buildLists2(self):
        self.pickType = ['Rank']
        self.pickSubType = ['Select']
    def updateSpinner2(self, text):
        global m
        if text == 'Rank':
            self.ids.rnk_spin_1.values = m
            self.ids.rnk_spin_2.values = m
            self.ids.rnk_spin_3.values = m
            self.ids.rnk_spin_4.values = m
            self.ids.rnk_spin_5.values = m
            self.ids.rnk_spin_6.values = m
        else:
            i = 0
            while i < len(m):
                self.ids.rnk_spin_2.values = m
                self.ids.rnk_spin_3.values = m
                self.ids.rnk_spin_4.values = m
                self.ids.rnk_spin_5.values = m
                self.ids.rnk_spin_6.values = m
                self.ids.rnk_spin_1.values = m
                #n = modules[:i] + modules[i+1:]
                if text == m[i]:
                    m.pop(i)
                    self.ids.rnk_spin_2.values = m
                    self.ids.rnk_spin_3.values = m
                    self.ids.rnk_spin_4.values = m
                    self.ids.rnk_spin_5.values = m
                    self.ids.rnk_spin_6.values = m
                    self.ids.rnk_spin_1.values = m
                i += 1
#If user makes a mistake to reset the spinners
    def reset(self,rnk_spin_1,rnk_spin_2,rnk_spin_3,rnk_spin_4,rnk_spin_5,rnk_spin_6):
        global m
        m = modules[:]
        self.rnk_spin_1.text = '6'
        self.rnk_spin_2.text = '5'
        self.rnk_spin_3.text = '4'
        self.rnk_spin_4.text = '3'
        self.rnk_spin_5.text = '2'
        self.rnk_spin_6.text = '1'
#------------------------------------------------------------------------------#
#Window to generate the study timetable
class StudyTTWindow(Screen):
#function to add to database making sure things are only
#added where there is currently nothing scheduled
    def add_study_db(mod,day,time):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Attendit",
        database="attendit"
        )
        mycursor = mydb.cursor(buffered=True)
        try:
            mycursor.execute("insert into student (id,mod_name,day,time) Select 0, %s,%s,%s Where not exists(select * from student where mod_name=%s and day = %s and time =%s)",(mod,day,time,mod,day,time))
            mydb.commit()
            number_of_rows= mycursor.execute("SELECT * FROM student")
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

#if error quit the app
            App.get_running_app().stop()
#Function for determining the hours to study based on rankings
    def ranks(self):
        global modules
        ranking = {}
        ranking[r_1] = 1
        ranking[r_2] = 2
        ranking[r_3] = 3
        ranking[r_4] = 4
        ranking[r_5] = 5
        ranking[r_6] = 6
        m = 0


        for item in ranking:
            if not item.isdigit():
                m= m + ranking[item]
        print('m',m)
        mod_hours = {}
        rnk = m
        hours_per_part = s_hours/m
        print('hpp',hours_per_part)
        hour_mod ={}
        z = 0

        while z < len(modules):
            y = ranking[modules[z]]
            if modules[z] in ranking and not modules[z].isdigit():
                print('ri',ranking[modules[z]])
                hour_mod[modules[z]] = y * hours_per_part
            z += 1
        print('hourmod',hour_mod)

        for r in modules:
            while rnk > 0:
                if ranking[r] == rnk:
                    mod_hours[r] = rnk/s_hours
                rnk = rnk - 1


#add to database
        for k in hour_mod:
            j=0
            print(k,hour_mod[k])
            while j < hour_mod[k]:
                print(j,hour_mod[k])
                StudyTTWindow.add_study_db(k,'Tuesday',j,)
                j += 1
#------------------------------------------------------------------------------#
#Window Manager class
class WindowManager(ScreenManager):
    pass
#------------------------------------------------------------------------------#
#Builder to load the kv file
kv = Builder.load_file("app.kv")
class MyMainApp(App):
    def build(self):
        return kv
#run the app
if __name__ == "__main__":
    MyMainApp().run()
