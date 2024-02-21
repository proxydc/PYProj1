import kivy
from kivy.app import App 
from kivy.uix.button import Button

class MyFirstKivyApp(App):
    def build(self):
        return Button()
if __name__ == "__main__":
    kv_app = MyFirstKivyApp()
    kv_app.run()