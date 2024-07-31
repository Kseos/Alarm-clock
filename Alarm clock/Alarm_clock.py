# -*- coding: utf-8 -*-
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
#from kivymd.uix.pickers import MDDatePicker
from datetime import datetime


class Alarm_clock(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return MDScreen()
 
 
 
if __name__ == "__main__":
    app = Alarm_clock()
    app.run()
        

