import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

from logic.tree import tree


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def plot(self):
        tree()


class WindowManager(ScreenManager):
    pass


sm = WindowManager()

kv = Builder.load_file('story_writer.kv')

screens = [MainWindow(name='main')]
for screen in screens:
    sm.add_widget(screen)

sm.current = 'main'


class Story_WriterApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    Story_WriterApp().run()