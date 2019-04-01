import pygame

pygame.init()

# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("GOL")


gridWidth=100
gridHeight=100

grid=[[0]*gridWidth]*gridHeight#create grid

def getSquare(x,y):
    if(x<0 or y<0 or x>=gridWidth or x>=gridHeight):
        return 0
    return grid[y][x]

def countNeighbors(x,y):
    count=0
    for i in range(-1,2):
        for j in range(-1,2) :
            if not(i==0 and j==0):
                count+=getSquare(x+i,y+j)




done=False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255,255,255))

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
pygame.quit()
