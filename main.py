import sys
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
import calculs

class MyInterface(FloatLayout):

    def cliquer(self):
        self.month = self.ids.month_cursor.value
        self.contamination = self.ids.contamination_cursor.value
        self.people, self.infected = calculs.inhabitants(self.month, self.contamination)
        if self.infected > self.people:
            self.infected = self.people
        self.sick = int(0.75*self.infected)
        self.healthy_carrier = int(0.25*self.infected)
        
        with self.canvas:
            Color(1., 0, 0)
            Rectangle(pos = self.pos, size=(800,500))

        for _ in range(self.people):
            Person(self.canvas)
        
        self.ids.reponse.text = str(self.people) + " inhabitants"
        self.ids.sick.text = str(self.sick) + " sick"
        self.ids.healthy_carrier.text = str(self.healthy_carrier) + " healthy carrier"
        self.ids.infected.text = str(self.infected) + " infected"

class Person(Widget):
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos = [random.randint(1,750), random.randint(1,425)]

        with self.canvas:
            Rectangle(source='perso.png', pos = self.pos, size=(30,55))

class PopulationApp(App):

    def build(self):
        self.load_kv('interface.kv')
        return MyInterface()

PopulationApp().run()
sys.exit()