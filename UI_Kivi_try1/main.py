import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name=ObjectProperty(None)
    email = ObjectProperty(None)
    pass
    '''
    def __init__(self,colnum=2,**kwargs):
        super(MyGrid,self).__init__(**kwargs)

        self.inside=GridLayout()
        self.inside.cols=2
        self.cols=colnum
        self.inside.add_widget(Label(text="First Name"))
        self.first_name=TextInput(multiline=False)
        self.inside.add_widget(self.first_name)

        self.inside.add_widget(Label(text="Last Name Name"))
        self.last_name=TextInput(multiline=False)
        self.inside.add_widget(self.last_name)

        self.inside.add_widget(Label(text="email"))
        self.email=TextInput(multiline=False)
        self.inside.add_widget(self.email)
        self.add_widget(self.inside)
        self.submit=Button(text="submit",font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    '''
    def pressed(self):
        #name=self.first_name.text
        #last=self.last_name.text
        #email=self.email.text

        print("name: ",self.name.text," email: ",self.email.text)
        self.name.text=""
        self.email.text = ""



class MyApp(App):
    def build(self):
        return MyGrid() #Label(text="allergy avoid")


if __name__=="__main__":
    MyApp().run()