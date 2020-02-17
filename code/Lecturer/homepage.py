from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
class MainWindow(Screen):
    pass

class Second(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("mytest.kv")

class MyTestApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyTestApp().run()