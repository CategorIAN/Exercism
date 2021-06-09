import random

class Robot:
	def __init__(self):
		self.alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.name = random.choice(self.alph) + random.choice(self.alph) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
		self.archive = []

	def reset(self):
		self.archive.append(self.name)
		while True:
			name = random.choice(self.alph) + random.choice(self.alph) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
			if (name not in self.archive):
				self.name = name
				break


		
		

		


