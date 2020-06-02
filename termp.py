from termcolor import colored
from PIL import Image 
import pickle
import math

class termp:
	p1 = [(200, "█"), (150, "▓"), (90, "▒"), (0, "░")]
	p2 = [(230, "#"), (207, "&"), (184, "$"), (161, "X"), (138, "x"), (115, "="), (92, "+"), (69, ";"), (46, ":"), (0, ".")]
	p3 = [(200, "▉"), (150, "▙"), (90, "▚"), (0, "▘")]
	
	def __init__(self, x=40, y=40, char="░"):
		self.array = [char for i in range(y*x)] 
		self.width, self.height = x, y
		self.x, self.y = 0, 0
		self.draw = True
	
	def point(self, x, y, char="█"):
		if 0 <= x < self.width and 0 <= y < self.height:
			self.array[x+y*self.width]= char
	
	def get(self, x, y):
		if 0 <= x < self.width and 0 <= y < self.height:
			return self.array[x+(y*self.width)]
		
	def __str__(self):
		return "\n".join(["".join([self.array[x] for x in range((y)*self.width,(y+1)*self.width)]) for y in range(self.height)])
	
	def print(self):
		print(str(self))
	
	def goto(self, x, y, char="█"):
		if self.draw: self.line(self.x, self.y, x, y, char)
		self.x, self.y = x, y
		
	def clear(self, char="░"):
		self.array = [char for i in range(self.width*self.height)] 
	
	def image(self, file, w=30, x=0, y=0, resize=True, color=False, chars=[(200, "█"), (150, "▓"), (90, "▒"), (0, "░")]):
		img = Image.open(file)
		if resize:
			img = img.resize((w, int((float(img.size[1]) * float((w / float(img.size[0])))))), Image.ANTIALIAS)
		img = img.convert('RGB', palette=Image.ADAPTIVE)
		pimg = img.load()
		for ix in range(img.size[0]):
			for iy in range(img.size[1]):
				R = pimg[ix, iy][0]
				G = pimg[ix, iy][1]
				B = pimg[ix, iy][2]
				if color:
					if G > R and B > R: C = "cyan"
					elif R > G and B > G: C = "magenta"
					elif R > B and G > B: C = "yellow"
					elif G < R > B: C = "red"
					elif B < G > R: C = "green"
					elif R < B > G: C = "blue"
					else: C = "white"
				S = (R+G+B) // 3
				for level, char in chars:
					if S > level:
						if color:
							self.point(x+ix, y+iy, colored(char, C))
						else:
							self.point(x+ix, y+iy, char)
						break
					
	def rect(self, x1=0, y1=0, x2=10, y2=10, char="█", fill=False):
		if fill:
			for y in range(y1, y2):
				for x in range(x1, x2):
					self.point(x, y, char)
		else:
			self.line(x1,y1,x2,y1, char)
			self.line(x2,y1,x2,y2, char)
			self.line(x2,y2,x1,y2, char)
			self.line(x1,y2,x1,y1, char)
	
	def givecolor(self, color):
		for x in range(self.width):
			for y in range(self.height):
				self.point(x, y, colored(self.get(x, y), color))
				
	def fill(self, x=0, y=0, char="█"):
		target_char = self.get(x, y)
		pos = [(x, y)]
		while len(pos) > 0: 
			x1, y1 = pos[-1]
			pos.pop()
			if self.get(x1+1, y1) == target_char:
				pos.append((x1 + 1, y1))
			if self.get(x1-1, y1) == target_char:
				pos.append((x1 - 1, y1))
			if self.get(x1, y1+1) == target_char: 
				pos.append((x1, y1 + 1))
			if self.get(x1, y1-1) == target_char:
				pos.append((x1, y1 - 1))
			if self.get(x1, y1) == target_char:
				self.point(x1, y1, char)
				
	def circle(self, x=10, y=10, radius=5, char="█", q=360, fill=False):
		for i in range(q):
			a = 2*math.pi*(i/q)
			if fill:
				self.line(x,y,int(math.cos(a)*radius)+x, int(math.sin(a)*radius)+y, char)
			else:
				self.point(int(math.cos(a)*radius)+x, int(math.sin(a)*radius)+y, char)
	
	def shape(self, x=10, y=10, radius=5, char="█", q=3):
		first = False
		for i in range(q):
			a = 2*math.pi*(i/q)
			xi = int(math.cos(a)*radius)+x
			yi = int(math.sin(a)*radius)+y
			if first:
				self.line(xs, ys, xi, yi, char)
			else:
				self.point(xi, yi, char)
				sx, sy = xi, yi
				first = True
			xs, ys = xi, yi
		self.line(xs, ys, sx, sy, char)
	
	def save(self, file="termp.pk"):
		with open(file, 'wb') as f:
			pickle.dump((self.array, self.width, self.height), f)
	
	def read(self, file="termp.pk"):
		with open(file, 'rb') as f:
			self.array, self.width, self.height = tuple(pickle.load(f))
	
	def export(self, file="termp.txt"):
		with open(file) as f:
			f.write(str(self))
			
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