from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Midnightblue'
        return Builder.load_file('album.kv')

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

if __name__ == "__main__":
    MainApp().run()
