from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import sys
sys.path.append('/.../')
import main_checks as mainact
import df_main_feches as db_m
import cv2

# kv = Builder.load_file("Alergies.kv")


class BoxLayoutExample(Screen):
    '''
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        b1=Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)'''
    pass


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        print("checking")
        my_db = db_m.db_matirials()

        img = cv2.imread("IMG_{}.png".format(timestr))
        image_checks = my_db.get_word_list('ISOTHIOAZOLINONE')
        ansin, isans,message = mainact.image_check(img, image_checks)
        if ansin:
            self.ids['lab'].text=message+"\n ok to use"
            self.ids['lab'].background_color = [1, 0, 0, 1]
            print("ok to use")
        else:
            self.ids['lab'].text = message+"\n Not good"
            print("Not good")


# class MainWidget(Screen):
#    pass

class WindowManeger(ScreenManager):
    pass


class AlergiesApp(App):
    # def build(self):
    #     return kv

    pass


AlergiesApp().run()
