# -*- coding: utf-8 -*-
import kivy 
from kivy.app import App
from kivy.uix.bubble import BoxLayout 

kivy.require('1.9.0')       
# '2.0.0.' стоит попробовать потом, зависит от телефона

class Alarm_clock(App):
    def build(self):
        return BoxLayout()
    
neuralRandom = Alarm_clock()
neuralRandom.run()
        

