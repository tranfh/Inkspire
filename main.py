from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.imagelist import SmartTileWithLabel
import glob
from kivymd.uix.label import MDLabel
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.list import OneLineIconListItem



class MainApp(MDApp):
    def on_start(self):
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = '100'

        # Load Images on Home Screen
        for filepath in glob.iglob(r'/Users/franktran/PycharmProjects/Inkspire/source/*.jpeg', recursive=True):
            print(filepath)
            self.load_image(filepath, "")

    def load_image(self, source, text):
        load_image = SmartTileWithLabel(source=source, text=text)
        self.root.ids.homelayout.add_widget(load_image)
MainApp().run()
