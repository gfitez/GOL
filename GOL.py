import pygame
import random, copy

pygame.init()

# Set the width and height of the screen [width, height]

size = (500, 500)

gridHeight = 25
gridWidth = 25



class Grid:
    def __init__(self):
        self.gridWidth=gridWidth
        self.gridHeight=gridHeight

        self.grid=[]
        for i in range(0,self.gridHeight):
            self.grid.append([0]*self.gridWidth)



        self.cellWidth=size[0]/self.gridWidth
        self.cellHeight=size[1]/self.gridHeight
    def getSquare(self, x,y):
        if(x<0 or y<0 or x>=self.gridWidth or y>=self.gridHeight):
            return 0
        else:
            return self.grid[y][x]

    def countNeighbors(self, x,y):
        count=0
        for i in range(-1,2):
            for j in range(-1,2) :
                if not(i==0 and j==0):
                    count+=self.getSquare(x+i,y+j)
        return count

    def displayGrid(self):
        for rowI in range(0,len(self.grid)):
            for cellI in range(0,len(self.grid[rowI])):
                if(self.grid[rowI][cellI]==1):
                    pygame.draw.rect(screen,(0,0,0),(cellI*self.cellWidth,rowI*self.cellHeight,self.cellWidth,self.cellHeight))
    def updateGrid(self):
        newGrid=[]
        aliveCount=0
        for rowI in range(0,len(self.grid)):
            newGrid.append([])
            for cellI in range(0,len(self.grid[rowI])):
                neighbors=self.countNeighbors(cellI,rowI)
                alive=0
                if(neighbors<2):
                    alive=0
                elif(self.grid[rowI][cellI]==1 and neighbors<=3):
                    alive=1
                elif(neighbors==3):
                    alive=1
                else:
                    alive=0
                newGrid[rowI].append(alive)
                aliveCount+=alive
        self.grid=newGrid
        return(aliveCount)
    def randomize(self):
        for rowI in range(0,len(self.grid)):
            for cellI in range(0,len(self.grid[rowI])):
                self.grid[rowI][cellI]=random.choice([0,1])
    def clear(self):
        for rowI in range(0,len(self.grid)):
            for cellI in range(0,len(self.grid[rowI])):
                self.grid[rowI][cellI]=0
    def randomizeRegion(self):
        self.clear()

class Animal:
    def __init__(self):
        self.map = []
        self.fitness = 0
        self.animalGrid = None
        for i in range(0,gridHeight):
            self.map.append([])
            for j in range(0,gridWidth):
                self.map[i].append(random.random())



    def createGrid(self):
        self.animalGrid = Grid()
        for i in range(0, gridHeight):
            for j in range(0, gridWidth):
                if self.map[i][j] > .5:
                    self.animalGrid.grid[i][j] = 1

    def calculateFitness(self, iterations):
        total = 0.0
        for i in range(iterations):
            total += self.animalGrid.updateGrid()

        self.fitness=self.animalGrid.updateGrid()
        #self.fitness = total/iterations

    def breed(self, other):
        aOut = Animal()
        for i in range(gridHeight):
            for j in range(gridWidth):
                if(random.random() > .5):
                    aOut.map[i][j] = self.map[i][j]
                else:
                    aOut.map[i][j] = other.map[i][j]
                if(random.random()>0.99):#random mutation
                    aOut.map[i][j]=random.random()
        return aOut


generation = [None] * 50
iterations = 20

for c in range(len(generation)):
     generation[c] = Animal()

def runGen():
    global generation
    tot = 0.0
    for c in range(len(generation)):
        generation[c].createGrid()
        generation[c].calculateFitness(iterations)
        tot += generation[c].fitness
    generation.sort(key=lambda x: -x.fitness)

    print(str(generation[0].fitness)+" "+str(tot/len(generation)))


    parents=generation[0:20]#get top performances
    nextGen=generation[0:5]#keep 4 best parents
    for i in range(2):
        for parent in parents:
            nextGen.append(parent.breed(random.choice(parents)))
            nextGen[len(nextGen)-1].createGrid()
    for i in range(5):
        newAnimal=Animal()
        newAnimal.createGrid()
        nextGen.append(newAnimal)
    generation=nextGen













done=False






screen = pygame.display.set_mode(size)

pygame.display.set_caption("GOL")

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    runGen()


    generation[0].createGrid()


    for i in range(iterations):
        screen.fill((255,255,255))
        pygame.time.wait(25)
        generation[0].animalGrid.updateGrid()
        generation[0].animalGrid.displayGrid()
        pygame.display.flip()


pygame.quit()
