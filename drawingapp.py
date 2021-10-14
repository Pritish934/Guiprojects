# pip instaall kivy to install the module
# import kivy 
from typing import Mapping
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

# Create a class Drawinput to make a drawing screen
class DrawInput(Widget):
    
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))
        
    def on_touch_move(self, touch):
        print(touch)
        touch.ud["line"].points += (touch.x, touch.y)
		
    def on_touch_up(self, touch):
        print("RELEASED!",touch)

# create a class to build the app
class SimpleKivy4(App):
    
    def build(self):
        return DrawInput()

# build the main function
if __name__ == "__main__":
    SimpleKivy4().run()
