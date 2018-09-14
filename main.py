from random import randint

class Organism:

	def move(self):
		print("stuff")


class ant(Organism):

	def move():
		print("t")



def genPositionsPred():

	x = randint(0, 19)
	y = randint(0, 19)
	i = 0
	position = (x, y)
	predL = [] 

	while i < 5:
		if position not in predL:
			predL.append(position)
			i += 1
		else:
			x = randint(0, 19)
			y = randint(0, 19)
			position = (x, y)




	return predL

def genPositionsPrey(predL):

	x = randint(0, 19)
	y = randint(0, 19)
	i = 0
	position = (x, y)
	preyL = [] 
	while i < 10:
		if position not in predL and position not in preyL:
			preyL.append(position)
			i += 1
		else:
			x = randint(0, 19)
			y = randint(0, 19)
			position = (x, y)




	return preyL

def printWorld(world):
	for j in range(0, 20):
		for z in range(0, 20):
			print(world[j][z], end=" ")

		print("")



obj = Organism()
obj.move()

world = [["-" for j in range(0, 20)] for z in range(0, 20)] 
predL = genPositionsPred()
preyL = genPositionsPrey(predL)


for j in predL:
	world[j[0]][j[1]] = "X"

for j in preyL:
	world[j[0]][j[1]] = "O"



printWorld(world)













