from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import mysql.connector
from mysql.connector import Error
from kivy.garden.matplotlib import FigureCanvasKivyAgg


import matplotlib.pyplot as plt 


x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x,y, label='Bars1', color='blue')
plt.bar(x2,y2, label='Bars2', color='c') 

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck It out')
plt.legend()


id_= {}



try:
	connection = mysql.connector.connect(
	  host="127.0.0.1",
	  database= 'attendit',
	  user="root",
	  passwd="6wijijo0"
	  
	)

	sql_select_Query = "select * FROM lecturer;"
	cursor = connection.cursor()
	cursor.execute(sql_select_Query)
	records = cursor.fetchall()
	print("Total no of rows in LAptop is: ", cursor.rowcount)

	print("\nPrinting each id record")
	for row in records:
		#print("idstudent =", row[0],)
		#print("name =", row[1],)
		#print("grade =", row[2],)
		
		if row[0] not in id_.keys():
			id_[row[0]] = row[1]
		#id_.append(row[0])
		#print("attendance =", row[3], "\n")
		#mod.append(row[1])
	print(id_)


except Error as e:
	print("Error reading data from MySql table", e)
finally:
	if (connection.is_connected()):
		connection.close()
		cursor.close()
		print("MySQL connection is closed")	
		#print(id_, mod)


class Progress(Screen):
	bar= ObjectProperty(None)

	def on_pre_enter(self, *args):
		self.bar.add_widget(FigureCanvasKivyAgg(plt.gcf()))
		self.manager.current = "analysis"



class MainWindow(Screen):
    username = ObjectProperty(None)
    passw = ObjectProperty(None)


   	

    def verify_credentials(self):
	    #for k in id_:
	    	#if str(k) == str(self.username.text) and str(id_[k]) == str(self.passw.text):
	    self.manager.current = "homepage"
	    self.username.text =""
	    self.passw.text= ""
    def btn(self):
    	print("Username: ", self.username.text, "password: ", self.passw.text )

    pass

class Second(Screen):
	
	pass

class Third(Screen):
	pass

class Fourth(Screen):
	pass

class Fifth(Screen):
	pass

class Grafico(Screen):
	def on_enter(self, *args):
		box = BoxLayout(orientation='vertical')
		box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
		self.add_widget(box)
		btn = Button(text='HOMEPAGE',
			size_hint=(.1,.1))
		box.add_widget(btn)
		#self.add_widget(btn)

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("mytest.kv")

class MyTestApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyTestApp().run()