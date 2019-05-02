from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class NameListerApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Jim', 'Jane', 'John', 'Joe', 'July']


    def build(self):
        self.title = "List of Names"
        self.root = Builder.load_file('name_lister.kv')
        self.create_widgets()
        return self.root


    def create_widgets(self):

        for name in self.names:
            temp_button = Button(text=name, id=name)
            self.root.ids.list_viewer.add_widget(temp_button)

NameListerApp()