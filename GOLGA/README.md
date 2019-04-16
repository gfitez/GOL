How to run:
1. [Download Processing](https://processing.org/download/)
2. Double click on the file GOLGA.pde to open it in processing
3. Click the play button in the top left corner
4. Follow the prompts to set the simulation parameters
	Itterations: the number of itterations to run in order to caluate each animals fitness
	Mutaion rate: percentage of mutaions (0, 1)
	Size: the number of animals in a genration MUST BE BIGGER THAN 20!
![Image Falied to Load](https://i.ibb.co/JrG84pL/Screenshot-3.png)
5. The program will run the simulation and try and optimize for the most number of lit squares given the parameters. The animation you see will be the top profomer from the last generation. The graph is the fitness over genrations and the concle will print the best and average for that gneration.
![Image Falied to Load](https://i.ibb.co/r0zq5BJ/Screenshot-2.png)

Notes: 
	We initially used python and the pyGame lib. This worked well but took a while to run each iteration due to pythons overhead and the fact that python is not intended to run a GUI. For these reasons, we chose to use a java based language called processing. It is a lot easier to read and understand while still allowing us to compute each iteration very quickly. 
	We used [this](https://www.youtube.com/watch?v=9zfeTw-uFCw&list=PLRqwX-V7Uu6bJM3VgzjNV5YxVxUwzALHV) playlist to help us inform our general approach and it also brought processing to our attention. 
	We currently calculate fitness by counting the number of lit pixels on the last frame. We also have the ablity to do the average across all frames. Our breeding takes the top 10 parrents and breeds each twice with the other top preformers to get 20 kids. It also keeps the best parrent. Then it adds new children in to get to size. When breeding it picks randomly one of the 2 values. If the float (0,1) is >.95 it is turned on for the first itteration. If mutation count is triggered it makes that value a random number (0,1)

Libs:
	We use Arrays and Scanner which are both built in java libs.
	
File: GOLGA.pde
This file contains the entire program. When run, it will continue to iterate through the genetic algorithm and graph the outcome.
 - Class: Grid
	This class contains the entirety of the game of life simulation. However, it does not contain any functions or data related to genetic algorithms. It also has a display and update function.
-Class: Animal
	This class is a representation of a single organism. It contains the organism's genetic data, the function to breed, as well as a Grid as instance data. It implements Comparable<Animal> so that we can easily compare 2 fitenesses. And thus sort easier.
-Function: RunGen
	This function is the bulk of the program. Using, the generation[] array, it will simulate all of the Animals, sort them, breed them and create the next Generation. See above for details.

