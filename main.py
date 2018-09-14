from random import randint

class Organism:

	def move(self):
		print("stuff")



class ant(Organism):

	def move(self):
		print("t")


class antSpider(Organism):
	
	def move(self):
		print("t")



def genPositionsPred():

	predL = [] 
	genPositionHelper(5, predL)

	return predL



def genPositionHelper(num, predL, preyL=None):
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




obj = ant()
obj.move()

world = [["-" for j in range(0, 20)] for z in range(0, 20)] 
predL = genPositionHelper(5, [])
preyL = genPositionHelper(10, predL, [])


for j in predL:
	world[j[0]][j[1]] = "X"

for j in preyL:
	world[j[0]][j[1]] = "O"



printWorld(world)













