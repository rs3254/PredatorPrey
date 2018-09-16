from random import randint

class Organism:

	def __init__(self, xCoordinate, yCoordinate):
		self.xCoordinate = xCoordinate		
		self.yCoordinate = yCoordinate
		# self.divide = 3


	def move(self, xCoordinate, yCoordinate):
		mV = randint(-1,1)
		mH = randint(-1,1)

		if mV == 0:
			xCoordinate += mH
		else:
			yCoordinate += mV






class ant(Organism):

	def __init__(self, xCoordinate, yCoordinate):
		super().__init__(xCoordinate, yCoordinate)

	def move(self):
		print("t")


class antSpider(Organism):

	def __init__(self, xCoordinate, yCoordinate):
		super().__init__(xCoordinate, yCoordinate)

	
	def move(self):
		print("t")






def genPosition(num, predL, preyL=None):
	i = 0
	x = randint(0, 19)
	y = randint(0, 19)
	position = (x, y)
	while i < num:
		if position not in predL and preyL == None:
			predL.append(position)
			i += 1
		elif position not in predL and position not in preyL:
			preyL.append(position)
			i += 1
		else:
			x = randint(0, 19)
			y = randint(0, 19)
			position = (x, y)

	return preyL or predL



def printWorld(world):
	for j in range(0, 20):
		for z in range(0, 20):
			print(world[j][z], end=" ")

		print("")





# contain objects
predArr = [] 
preyArr = [] 

world = [["-" for j in range(0, 20)] for z in range(0, 20)] 
predL = genPosition(5, [])
preyL = genPosition(10, predL, [])



for j in predL:
	world[j[0]][j[1]] = "X"
	print(j[1], j[0])
	spider = antSpider(j[1], j[0])
	predArr.append(spider)

for j in preyL:
	world[j[0]][j[1]] = "O"
	antObj = ant(j[1], j[0])
	preyArr.append(antObj)



printWorld(world)
for j in predArr:
	print(j.xCoordinate)













