from termcolor import colored
import pickle
import math

class termp:
	def __init__(self, x=40, y=40, char="░"):
		self.array = [char for i in range(y*x)] 
		self.width, self.height = x, y
		self.x, self.y = 0, 0
		self.draw = True
		
	def point(self, x, y, char="█"):
		self.array[x+(y*self.height)]= char
		
	def text(self):
		return "\n".join(["".join([self.array[x] for x in range((y)*self.width,(y+1)*self.width)]) for y in range(self.height)])
	
	def print(self):
		print(self.text())
	
	def goto(self, x, y, char="█"):
		if self.draw: self.line(self.x, self.y, x, y, char)
		self.x, self.y = x, y
		
	def clear(self, char="░"):
		self.array = [char for i in range(self.width*self.height)] 
	
	def rect(self, x1=0, y1=0, x2=10, y2=10, char="█", fill=False):
		if fill:
			for y in range(y1, y2):
				for x in range(x1, x2):
					self.point(x, y, char)
		else:
			self.line(x1,y1,x2,y1)
			self.line(x2,y1,x2,y2)
			self.line(x2,y2,x1,y2)
			self.line(x1,y2,x1,y1)
	
	def circle(self, x=10, y=10, radius=5, char="█", q=360, fill=False):
		for i in range(q):
			a = 2*math.pi*(i/q)
			if fill:
				self.line(x,y,int(math.cos(a)*radius)+x, int(math.sin(a)*radius)+y, char)
			else:
				self.point(int(math.cos(a)*radius)+x, int(math.sin(a)*radius)+y, char)
	
	def save(self, file="termp.pk"):
		with open(file, 'wb') as f:
			pickle.dump(self.array, f)
	
	def read(self, file="termp.pk"):
		with open(file, 'rb') as f:
			self.array = list(pickle.load(f))
	
	def export(self, file="termp.txt"):
		with open(file) as f:
			f.write(self.text())
			
	def line(self, x1=0, y1=0, x2=10, y2=10, char="█"):
		delta_x, delta_y = abs(x2 - x1), abs(y2 - y1)
		sign_x = 1 if x1 < x2 else -1
		sign_y = 1 if y1 < y2 else -1
		error = delta_x - delta_y
		self.point(x2, y2,char)
		while (x1 != x2 or y1 != y2):
			self.point(x1, y1,char)
			error_2 = error * 2
			if error_2 > -delta_y:
				error -= delta_y
				x1 += sign_x
			if error_2 < delta_x:
				error += delta_x
				y1 += sign_y