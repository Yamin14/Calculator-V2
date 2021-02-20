import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from math import *

class Calculator(GridLayout):
	def __init__(self, **kwargs):
		super(Calculator, self).__init__(**kwargs)
		self.bg = (0.529, 0.808, 0.922, 1)
		self.fg = (0, 1, 1, 1)
		self.width = 150
		self.height = 150
		self.font_size = 70
		self.x, self.y = 20, 200
		
		self.buttons = []
		for i in range(10):
			self.buttons.append(Button(text=str(i), background_color=self.bg, color=self.fg, pos=(self.x, self.y), size=(self.width, self.height), font_size=self.font_size))
			if i >= 1:
				if self.x <= 300:
					self.x += 150
				else:
					self.x = 20
					self.y += 150
					
		for i in range(10, 26):
			if i == 10:
				self.text = "."
			elif i == 11:
				self.text = "="
			elif i == 12:
				self.text = "+"
			elif i == 13:
				self.text = "-"
			elif i == 14:
				self.text = "×"
			elif i == 15:
				self.text = "÷"
			elif i == 16:
				self.text = "Clear"
			elif i == 17:
				self.text = "Delete"
			elif i == 18:
				self.text = "("
			elif i == 19:
				self.text = ")"
			elif i == 20:
				self.text = "^"
			elif i == 21:
				self.text = "!"
			elif i == 22:
				self.text = "sin("
			elif i == 23:
				self.text = "cos("
			elif i == 24:
				self.text = "tan("
			elif i == 25:
				self.text = "π"
		
			self.buttons.append(Button(text=self.text, background_color=self.bg, color=self.fg, size=(self.width, self.height), font_size=self.font_size))
			
		self.buttons[0].pos = (170, 50)
		self.buttons[10].pos = (20, 50)
		self.buttons[11].pos = (320, 50)
		self.buttons[12].pos = (470, 500)
		self.buttons[13].pos = (470, 350)
		self.buttons[14].pos = (470, 200)
		self.buttons[15].pos = (470, 50)
		self.buttons[16].pos = (20, 650)
		self.buttons[17].pos = (320, 650)
		self.buttons[18].pos = (170, 750)
		self.buttons[19].pos = (320, 750)
		self.buttons[20].pos = (20, 750)
		self.buttons[21].pos = (470, 750)
		self.buttons[22].pos = (20, 900)
		self.buttons[23].pos = (220, 900)
		self.buttons[24].pos = (420, 900)
		self.buttons[25].pos = (620, 50)
		
		self.buttons[16].size = (300, 100)
		self.buttons[17].size = (300, 100)
		self.buttons[22].size = (200, 100)
		self.buttons[23].size = (200, 100)
		self.buttons[24].size = (200, 100)
		self.buttons[25].size = (100, 150)
		
		for i in range(26):
			self.add_widget(self.buttons[i])
			if self.buttons[i].text != "=" and self.buttons[i].text != "Delete" and self.buttons[i].text != "Clear" and self.buttons[i].text != "^" and self.buttons[i].text != "÷" and self.buttons[i].text != "×" and self.buttons[i].text != "!" and self.buttons[i].text != "sin(" and self.buttons[i].text != "cos(" and self.buttons[i].text != "tan(":
				self.buttons[i].bind(on_press=self.pressed)
			elif self.buttons[i].text == "Delete":
				self.buttons[i].bind(on_press=self.delete)
			elif self.buttons[i].text == "Clear":
				self.buttons[i].bind(on_press=self.clear)
			elif self.buttons[i].text == "=":
				self.buttons[i].bind(on_press=self.equal)
			elif self.buttons[i].text == "^":
				self.buttons[i].bind(on_press=self.power)
			elif self.buttons[i].text == "÷":
				self.buttons[i].bind(on_press=self.divide)
			elif self.buttons[i].text == "×":
				self.buttons[i].bind(on_press=self.multiply)
			elif self.buttons[i].text == "sin(":
				self.buttons[i].bind(on_press=self.trig)
			elif self.buttons[i].text == "cos(":
				self.buttons[i].bind(on_press=self.trig)
			elif self.buttons[i].text == "tan(":
				self.buttons[i].bind(on_press=self.trig)
			if self.buttons[i].text == "!":
				self.buttons[i].bind(on_press=self.fact)
			
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
		
	def power(self, instance):
		self.input_label.text += "**"
		
	def multiply(self, instance):
		self.input_label.text += "*"
		
	def divide(self, instance):
		self.input_label.text += "/"
		
	def fact(self, instance):
		self.input_label.text += "!"
		self.num = ""
		self.i = self.input_label.text.index("!")

		while "+" not in self.num and "-" not in self.num and "*" not in self.num and "/" not in self.num and "(" not in self.num and ")" not in self.num and "!" not in self.num and self.i >= 0:
			self.i -= 1
			self.num += self.input_label.text[self.i]
			
		if self.i < 0:
			self.num = self.num[:-1] 
		self.num = self.num[::-1]
		try:
			self.num = int(self.num)
			
			self.fact_ans = str(factorial(self.num))
			self.start_pos = self.i + 1
			self.end_pos = self.input_label.text.index("!")
			
		except:
			pass

	def trig(self, instance):
		pass
		
	def equal(self, instance):
		try:
			if "!" not in self.input_label.text:
				self.expression = self.input_label.text
			elif "!" in self.input_label.text:
				self.expression = self.input_label.text[:self.start_pos] + self.fact_ans + self.input_label.text[self.end_pos+1:]
				
			if "π" in self.input_label.text:
				pos = 0
				for i in self.input_label.text:
					if i == "π":
						self.expression = self.input_label.text[:pos] + str(pi) + self.input_label.text[pos+1:]
					pos += 1
			
			self.answer = eval(self.expression)
		except:
			self.answer = "ERROR"
			
		self.result_label.text = str(self.answer)

class MyApp(App):
	def build(self):
		return Calculator()
		
if __name__ == "__main__":
	MyApp().run()
