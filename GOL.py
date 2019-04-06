import pygame
import random, copy
from grid import Grid


pygame.init()

# Set the width and height of the screen [width, height]

size = (500, 500)

gridHeight = 25
gridWidth = 25





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
        self.animalGrid = Grid(gridWidth,gridHeight,size)
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
iterations = 100

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


    for i in range(iterations+1):
        screen.fill((255,255,255))
        pygame.time.wait(25)
        generation[0].animalGrid.updateGrid()
        generation[0].animalGrid.displayGrid(screen)
        pygame.display.flip()


pygame.quit()
