class Domino:
	def __init__(self, side1, side2):
		self.side1 = side1
		self.side2 = side2
	def side(self):
		sides = (self.side1,self.side2)
		return sides

def createDominoObjects(myDominoes):
	dominoes = []
	for x in range(1,15):
		dominoes.append(Domino(myDominoes[x][0], myDominoes[x][1]))
	return dominoes

if __name__ == "__main__":
	print("Start")
	myDominoes = [(9,6),(4,3),(1,9),(12,4),(11,7),(12,6),(12,9),(10,12),(7,9),(11,4),(7,11),(8,2),(7,5),(5,1),(9,3)]
	dominoes = createDominoObjects(myDominoes)
	for x in range(0, 14):
		print(dominoes[x].side())

