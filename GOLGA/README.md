How to run:
1. Download Processing: https://processing.org/download/
2. Double click on the file GOLGA.pde to open it in processing
3. Click the play button in the top left corner
4. Follow the prompts to set the simulation parameters
5. The program will run the simulation and try and optimize for the most number of lit squares given the parameters.

File:GOLGA.pde
This file contains the entire program. When run, it will continue to iterate through the genetic algorithm and graph the outcome.
 - Class: Grid
	This class contains the entirety of the game of life simulation. However, it does not contain any functions or data related to the genetic algorithms.
-Class: Animal
	This class is a represntation of a single organism. It contains the organism's genetic data, the function to breed, as well as a Grid as instance data.
-Function: RunGen
	This function is the bulk of the program. Using, the generation[] array, it will simulate all of the Animals, sort them, breed them and create the next Generation.