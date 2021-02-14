import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Calculator(GridLayout):
	def __init__(self, **kwargs):
		super(Calculator, self).__init__(**kwargs)
		self.bg = (0.529, 0.808, 0.922, 1)
		self.fg = (0, 1, 1, 1)
		self.width = 150
		self.height = 150
		self.font_size = 70
		self.x, self.y = 70, 300
		
		self.buttons = []
		for i in range(10):
			self.buttons.append(Button(text=str(i), background_color=self.bg, color=self.fg, pos=(self.x, self.y), size=(self.width, self.height), font_size=self.font_size))
			if i >= 1:
				if self.x <= 300:
					self.x += 150
				else:
					self.x = 70
					self.y += 150
					
		for i in range(10, 20):
			if i == 10:
				self.text = "."
			elif i == 11:
				self.text = "="
			elif i == 12:
				self.text = "+"
			elif i == 13:
				self.text = "-"
			elif i == 14:
				self.text = "*"
			elif i == 15:
				self.text = "/"
			elif i == 16:
				self.text = "Clear"
			elif i == 17:
				self.text = "Delete"
			elif i == 18:
				self.text = "("
			elif i == 19:
				self.text = ")"
				
			self.buttons.append(Button(text=self.text, background_color=self.bg, color=self.fg, size=(self.width, self.height), font_size=self.font_size))
			
		self.buttons[0].pos = (220, 150)
		self.buttons[10].pos = (70, 150)
		self.buttons[11].pos = (370, 150)
		self.buttons[12].pos = (520, 600)
		self.buttons[13].pos = (520, 450)
		self.buttons[14].pos = (520, 300)
		self.buttons[15].pos = (520, 150)
		self.buttons[16].pos = (70, 750)
		self.buttons[17].pos = (370, 750)
		self.buttons[18].pos = (220, 850)
		self.buttons[19].pos = (370, 850)
		
		self.buttons[16].size = (300, 100)
		self.buttons[17].size = (300, 100)
		
		for i in range(20):
			self.add_widget(self.buttons[i])
			if self.buttons[i].text != "=" and self.buttons[i].text != "Delete" and self.buttons[i].text != "Clear":
				self.buttons[i].bind(on_press=self.pressed)
			elif self.buttons[i].text == "Delete":
				self.buttons[i].bind(on_press=self.delete)
			elif self.buttons[i].text == "Clear":
				self.buttons[i].bind(on_press=self.clear)
			elif self.buttons[i].text == "=":
				self.buttons[i].bind(on_press=self.equal)
			
		self.input_label = Label(text="", color=self.fg, pos=(320, 1200), font_size=40)
		self.add_widget(self.input_label)
		
		self.result_label = Label(text="", color=self.fg, pos=(370, 1050), font_size=70)
		self.add_widget(self.result_label)
		
	def pressed(self, instance):
		self.input_label.text += instance.text
	
	def delete(self, instance):
		self.input_label.text = self.input_label.text[:-1]
		
	def clear(self, instance):
		self.input_label.text = ""
		
	def equal(self, instance):
		try:
			self.answer = eval(self.input_label.text)
		except:
			self.answer = "ERROR"
			
		self.result_label.text = str(self.answer)

class MyApp(App):
	def build(self):
		return Calculator()
		
if __name__ == "__main__":
	MyApp().run()
