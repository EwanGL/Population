import sys
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
import calculs

class MyInterface(FloatLayout):

    def cliquer(self):
        with self.canvas:
            Color(1., 0, 0)
            Rectangle(pos = self.pos, size=(800,500))

        month = self.ids.cursor.value
        self.people = calculs.inhabitants(month)
        for _ in range(self.people):
            Person(self.canvas)
        self.ids.reponse.text = str(self.people) + " inhabitants"

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