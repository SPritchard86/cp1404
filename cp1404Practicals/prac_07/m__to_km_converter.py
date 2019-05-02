from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

KMS_IN_MILE = 1.60934

class ConvertMilesToKmApp(App):
    """Convert an input of Miles into Kilometers with a Kivy GUI"""

    def build(self):
        Window.size = (800, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('m_km_converter.kv')
        return self.root

    def convert_miles_to_km(self):
        miles = self.convert_str_to_float()
        km = miles * KMS_IN_MILE
        self.root.ids.km_display.text = str(km)

    def handle_increment(self, change):
        value = self.convert_str_to_float() + change
        self.root.ids.input_miles.text = str(value)
        self.convert_miles_to_km()


    def convert_str_to_float(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0


ConvertMilesToKmApp().run()
