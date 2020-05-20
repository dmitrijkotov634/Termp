from termcolor import colored
from PIL import Image
import math

class chars:
	q1 = "█"
	q2 = "▓"
	q3 = "▒"
	q4 = "░"
	
class termp:
	def __init__(self, x=40, y=40, char="░"):
		self.array = [char for i in range(y*x)] 
		self.canvas_x, self.canvas_y = x, y
		self.x, self.y = 0, 0
		self.draw = True
		
	def point(self, x, y, char="█"):
		self.array[x+(y*self.canvas_y)]= char
		
	def text(self):
		return "\n".join(["".join([self.array[x] for x in range((y)*self.canvas_x,(y+1)*self.canvas_x)]) for y in range(self.canvas_y)])
	
	def print(self):
		print(self.text())
	
	def goto(self, x, y, char="█"):
		if self.draw: self.line(self.x, self.y, x, y, char)
		self.x, self.y = x, y
		
	def clear(self, char="░"):
		self.array = [char for i in range(self.canvas_x*self.canvas_y)] 
	
	def rect(self, x1=0, y1=0, x2=10, y2=10, char="█"):
		for y in range(y1, y2):
			for x in range(x1, x2):
				self.point(x, y, char)
	
	def circle(self, x=10, y=10, radius=5, char="█", q=360, fill=False):
		for i in range(q):
			a = 2*math.pi*(i/q)
			if fill:
				self.line(x,y,int(math.cos(a)*radius)+x, int(math.sin(a)*radius)+y, char)
			else:
				self.point(int(math.cos(a)*radius)+x, int(math.sin(a)*radius)+y, char)
	
	def save(self, file="termp.txt"):
		with open(file) as f: f.write(self.text())
	
	def read(self, file="termp.txt"):
		self.array = []
		with open(file) as f:
			data = f.read().split("\n")
			self.canvas_y = len(data)
			self.canvas_x = len(data[0])
			for i in data:
				self.array += list(i)
			
	def image(self, file, w=30, x=0, y=0, resize=True):
		img = Image.open(file)
		if resize:
			img = img.resize((w, int((float(img.size[1]) * float((w / float(img.size[0])))))), Image.ANTIALIAS)
		pix = img.load()
		for ix in range(img.size[0]):
			for iy in range(img.size[1]):
				r,g,b = pix[x, y][0], pix[x, y][1], pix[x, y][2]
				s = (r + g + b) // 3
				if s > 220:
					print(r,g,b)
					self.point(x+ix, y+iy, "█")
				elif s > 170:
					self.point(x+ix, y+iy, "▓")
				elif s > 80:
					self.point(x+ix, y+iy, "▒")
				else:
					self.point(x+ix, y+iy, "░")
					
	def line(self, x1=0, y1=0, x2=10, y2=10, char="█"):
		delta_x = abs(x2 - x1)
		delta_y = abs(y2 - y1)
		if x1 < x2:
			sign_x = 1
		else:
			sign_x = -1
		if y1 < y2:
			sign_y = 1
		else:
			sign_y = -1
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