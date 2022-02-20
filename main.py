from kivy.app import App
from kivy.lang import Builder

kv = '''
Screen:
	canvas:
		Color:
			rgb:1,1,1
		Rectangle:
			pos:self.pos
			size:self.size
	Label:
		halign:'center'
		text:'[size=100][color=A155E7]hello world[/color][/size]'
		pos_hint:{'center_x':.5,'center_y':.5}
		size_hint_y:None
		height:self.texture_size[1]
		markup:True

'''
class App(App):
	def build(self):
		return Builder.load_string(kv)			
App().run()