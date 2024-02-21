import kivy
from kivy.app import App 
from kivy.uix.button import Label

class HelloKivy(App):#i. app creation
    def click_python(self, instance, value):
        print('User click on pyhton')
    def build(self):#2. build creation
        l= Label(text='[color=ff3333][i]Welcome[/i][/color] to [b]my first gui app[/b] in [ref=Python]python[/ref]',
                     font_size = '30sp',
                     markup = True
                     )
        l.bind(on_ref_press = self.click_python)
        return l

kivyApp = HelloKivy()
kivyApp.run()#3. running app