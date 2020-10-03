import sys
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
import calculs

class MyInterface(FloatLayout):

    def cliquer(self):
        month = self.ids.cursor.value
        self.people = calculs.inhabitants(month)
        for _ in range(self.people):
            Person(self.canvas)
    
class Person(Widget):
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos = [random.randint(1,800), random.randint(1,425)]

        with self.canvas:
            Rectangle(source='perso.png', pos = self.pos, size=(30,55))

class PopulationApp(App):
    
    def build(self):
        self.load_kv('interface.kv')
        return MyInterface()  
       
PopulationApp().run()
sys.exit()