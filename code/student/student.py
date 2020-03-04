from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty,ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from functools import partial
import json
import random
import mysql.connector
#------------------------------------------------------------------------------#
modules =[]
times = ['06h-07h','07h-08h','08h-09h','09h-10h','10h-11h','11h-12h','12h-13h','13h-14h','14h-15h','15h-16h','16h-17h','17h-18h','18h-19h','19h-20h','20h-21h','21h-22h','22h-23h','24h-00h']
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
hours_taken_up = 0
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
    hours_taken_up = mycursor.rowcount
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
class ExtraWindow(Screen):
#     def add_study_db(mod,day,time):
#         mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd="Attendit",
#         database="attendit"
#         )
#         mycursor = mydb.cursor(buffered=True)
#         try:
#             mycursor.execute("insert into student (id,mod_name,day,time) Select 0, %s,%s,%s Where not exists(select * from student where day = %s and time =%s)",(mod,day,time,day,time))
#             mydb.commit()
#         except mysql.connector.Error as err:
#             print("Something went wrong: {}".format(err))
#
# #if error quit the app
#             App.get_running_app().stop()
    def index():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Attendit",
        database="attendit"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT time,id,mod_name,day FROM student order by day,time")

        row_headers=[x[0] for x in mycursor.description]

        rv = mycursor.fetchall()

        global json_data
        json_data=[]
        d = {}
        for result in rv:
            f = result[2]
            x = row_headers[2]
            d=dict(mod_name=result[2])
            inv_map = {v: k for k, v in d.items()}
            json_data.append(inv_map)

        return json_data
#Class for ranking modules page
class ThirdWindow(Screen):
#When button pressed make sure hours per week is between 0 and 41
    def prs(self):
        global hours_taken_up
        if self.hours.text.isdigit() and 0 < int(self.hours.text) <= (126-hours_taken_up):
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
        self.rnk_spin_1.text = '1'
        self.rnk_spin_2.text = '2'
        self.rnk_spin_3.text = "3"
        self.rnk_spin_4.text = '4'
        self.rnk_spin_5.text = '5'
        self.rnk_spin_6.text = '6'
#------------------------------------------------------------------------------#

class CLabel(ToggleButton):
    bgcolor = ListProperty()


class HeaderLabel(Label):
    bgcolor = ListProperty()


class DataGrid(GridLayout):
    def __init__(self, header_data, cols_size, **kwargs):
        super(DataGrid, self).__init__(**kwargs)
        self.rows = 0
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))
        self.cols = len(header_data)
        self.spacing = [1, 1]
        self.counter = 0
        n = 0
        for hcell in header_data:
            header_str = "[b]" + str(hcell) + "[/b]"
            self.add_widget(HeaderLabel(text=header_str, markup=True, size_hint_y=None,
                                        height=40, id="Header_Label", size_hint_x=cols_size[n],
                                        bgcolor=[0.108, 0.476, 0.611]))
            n += 1

    def add_row(self, row_data, row_align, cols_size):
        self.rows += 1

        def change_on_press(clabel):
            childs = clabel.parent.children
            for ch in childs:
                if ch.id == clabel.id:
                    row_n = ch.id[4:5] if len(ch.id) == 11 else ch.id[4:6]
                    for c in childs:
                        if ('row_' + str(row_n) + '_col_') in c.id:
                            change_on_release(c)

        def change_on_release(clabel):
            clabel.state = "down" if clabel.state == "normal" else "normal"

        n = 0
        for item in row_data:
            cell = CLabel(text=('[color=000000]' + item + '[/color]'),
                          # background_color_normal=ListProperty([1, 1, 1, 0.5]),
                          # background_color_down = ListProperty([1, 1, 1, 1])
                          background_normal="background_normal.png",
                          background_down="background_pressed.png",
                          bgcolor=[1, 1, 1],
                          halign=row_align[n],
                          markup=True,
                          on_press=partial(change_on_press),
                          on_release=partial(change_on_release),
                          text_size=(0, None),
                          size_hint_x=cols_size[n],
                          size_hint_y=None,
                          height=40,
                          id=("row_" + str(self.counter) + "_col_" + str(n)))
            cell_width = Window.size[0] * cell.size_hint_x
            cell.text_size = (cell_width - 30, None)
            cell.texture_update()
            self.add_widget(cell)
            n += 1
        self.counter += 1

    # self.rows += 1
    def remove_row(self, n_cols, instance, **kwargs):
        childs = self.parent.children
        selected = 0
        for ch in childs:
            for c in reversed(ch.children):
                if c.id != "Header_Label":
                    if c.state == "down":
                        self.remove_widget(c)
                        selected += 1
        if selected == 0:
            for ch in childs:
                count = 0
                while count < n_cols:
                    if n_cols != len(ch.children):
                        for c in ch.children:
                            if c.id != "Header_Label":
                                self.remove_widget(c)
                                count += 1
                                break
                            else:
                                break
                    else:
                        break

    def select_all(self, instance, **kwargs):
        self.change_state("down")

    def unselect_all(self, instance, **kwargs):
        self.change_state("normal")

    def change_state(self, state):
        childs = self.parent.children
        for ch in childs:
            for c in ch.children:
                if c.id != "Header_Label":
                    c.state = state


class Table(BoxLayout,Screen):
    def __init__(self, head=['6h-7h','7h-8h','8h-9h','9h-10h','10h-11h','11h-12h','12h-13h','13h-14h','14h-15h','15h-16h','16h-17h','17h-18h','18h-19h','19h-20h','20h-21h','21h-22h','22h-23h','24h-00h'], **kwargs):
        super(Table, self).__init__(orientation="vertical")
        self.col_size = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        header = ['6h-7h','7h-8h','8h-9h','9h-10h','10h-11h','11h-12h','12h-13h','13h-14h','14h-15h','15h-16h','16h-17h','17h-18h','18h-19h','19h-20h','20h-21h','21h-22h','22h-23h','24h-00h']
        self.grid = DataGrid(header, self.col_size)
        self.grid.rows = 10
        scroll = ScrollView(size_hint=(1, 1), size=(4000, 500), scroll_x=0, pos_hint={'center_x': .5, 'center_y': .5})
        scroll.add_widget(self.grid)
        scroll.do_scroll_x, scroll.do_scroll_y = False, False
        self.add_widget(scroll)
        data_json = ExtraWindow.index()

        self.fill(data_json)

    def fill(self, data):
        body_alignment = ["center", "center", "center", "center","center", "center", "center", "center","center", "center", "center", "center","center", "center", "center", "center","center", "center"]
        for d in data:
            self.grid.add_row(d, body_alignment, self.col_size)
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
            mycursor.execute("insert into xtra(id,ame,day,time) Select 0, %s,%s,%s Where not exists(select * from student where day = %s and time =%s)",(mod,day,time,day,time))
            mydb.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

#if error quit the app
            App.get_running_app().stop()
    def count_db_rows():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Attendit",
        database="attendit"
        )
        mycursor = mydb.cursor(buffered=True)
        try:
            mycursor.execute("SELECT count(*) from student")
            mydb.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

#if error quit the app
            App.get_running_app().stop()
        return mycursor.fetchall()

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

        mod_hours = {}
        rnk = m
        try:
            hours_per_part = s_hours/m
        except:
            self.manager.current = 'study'

        hour_mod ={}
        z = 0

        while z < len(modules):
            y = ranking[modules[z]]
            if modules[z] in ranking and not modules[z].isdigit():

                hour_mod[modules[z]] = y * hours_per_part
            z += 1
        #print('hourmod',hour_mod)

        for r in modules:
            while rnk > 0:
                if ranking[r] == rnk:
                    mod_hours[r] = rnk/s_hours
                rnk = rnk - 1

#add to database
        for k in hour_mod:
            j=0
            #print(k,hour_mod[k])
            while j < hour_mod[k]:
                #print(j,hour_mod[k])
                d = random.choice(days)
                t = random.choice(times)
                if StudyTTWindow.add_study_db(k,d,t,) == 0:
                    hour_mod[k] += 1
                j += 1
        while StudyTTWindow.count_db_rows()[0][0] < 126:
            d = random.choice(days)
            t = random.choice(times)
            StudyTTWindow.add_study_db('',d,t,)
        return Table()

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
