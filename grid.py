import pygame
class Grid:
    def __init__(self,width,height,size):
        self.gridWidth=width
        self.gridHeight=height

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

    def displayGrid(self,screen):
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
