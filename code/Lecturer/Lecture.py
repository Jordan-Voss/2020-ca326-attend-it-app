from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
import mysql.connector
from mysql.connector import Error
from kivy.garden.matplotlib import FigureCanvasKivyAgg
import requests
import numpy as np
import matplotlib.pyplot as plt 



grades = []
attendance= []

def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 

def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    #plt.show() 









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
		#self.bar.add_widget(FigureCanvasKivyAgg(plt.gcf()))
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
	devices = ObjectProperty(None)
	
	def collect(self):
		
		r = requests.get('http://192.168.4.1')
	
		print(r.text)
		
	pass

class Third(Screen):
	def collect(self):
		
		r = requests.get('http://192.168.4.1')
	
		return r.text

	

	pass

class Fourth(Screen):
	pass

class Fifth(Screen):
	pass

class Grafico(Screen):
	

	def on_enter(self, *args):
		x = np.array(grades)
		y= np.array(attendance)
		b = estimate_coef(x,y)
		plot_regression_line(x,y,b)

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