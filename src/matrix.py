class Matrix:
	def __init__(self):
		self.m = list()
		for y in range(6):
			n = list()
			for x in range(7):
				n.append(int())
			self.m.append(n)

	def show():
		for y in self.m:
			print(y)

	def add(self, value, x):
		for y in range(6):
			y = 5-y
			if self.m[y][x] == 0:
				self.m[y][x] = value
				return y

	def solve_s(self):
		self.s = list()
		for y in range(7):
			n = list()
			for x in range(6): n+=[self.m[x][y]]
			self.s.append(self.s)
		for y in range(6):
			n = list()
			for x in range(7): n+=[self.m[y][x]]
			self.s.append(self.s)

		self.s+=[[self.m[2][0],self.m[3][1],self.m[4][2],self.m[5][3]]]
		self.s+=[[self.m[1][0],self.m[2][1],self.m[3][2],self.m[4][3],self.m[5][4]]]
		self.s+=[[self.m[0][0],self.m[1][1],self.m[2][2],self.m[3][3],self.m[4][4],self.m[5][5]]]
		self.s+=[[self.m[0][1],self.m[1][2],self.m[2][3],self.m[3][4],self.m[4][5],self.m[5][6]]]
		self.s+=[[self.m[0][2],self.m[1][3],self.m[2][4],self.m[3][5],self.m[4][6]]]
		self.s+=[[self.m[0][3],self.m[1][4],self.m[2][5],self.m[3][6]]]

		self.s+=[[self.m[3][0],self.m[2][1],self.m[1][2],self.m[0][3]]]
		self.s+=[[self.m[4][0],self.m[3][1],self.m[2][2],self.m[1][3],self.m[0][4]]]
		self.s+=[[self.m[5][0],self.m[4][1],self.m[3][2],self.m[2][3],self.m[1][4],self.m[0][5]]]
		self.s+=[[self.m[5][1],self.m[4][2],self.m[3][3],self.m[2][4],self.m[1][5],self.m[0][6]]]
		self.s+=[[self.m[5][2],self.m[4][3],self.m[3][4],self.m[2][5],self.m[1][6]]]
		self.s+=[[self.m[5][3],self.m[4][4],self.m[3][5],self.m[2][6]]]

	def control_victory(self):
		self.solve_s()
		for p in self.s:
			c = int()
			for x in range(len(p)-1):
				if p[x] == p[x+1] and not p[x] == int(): c+=1
				else: c = int()
				if c == 3: return True
		return False

	def show(self):
		for y in self.m:
			print(y)
