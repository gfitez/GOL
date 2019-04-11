import java.util.Arrays;
PrintWriter output;

int iterations = 50;
int boardWidth=50;
int boardHeight=50;
float mutationRate=0.001;
int parentCount=10;
int keeperCount=1;
int genSize=100;
int realChildren = 20;
ArrayList<Float> history = new ArrayList<Float>();

class Grid{
  int gridWidth, gridHeight;
  int screenW, screenH;
  int cellWidth, cellHeight;
  int[][] grid;
  
  
  Grid(int width, int height){
    gridWidth=width;
    gridHeight=height;
    screenW=500;
    screenH=500;
    cellWidth=screenW/gridWidth;
    cellHeight=screenH/gridHeight;
    
    
    grid=new int[gridHeight][];
    for(int i=0;i<gridHeight;i++){
      grid[i]=new int[gridWidth]; 
    }
  }
  
  public int getSquare(int x,int y){
    if(x<0 || y<0 || x>=gridWidth || y>=gridHeight) return 0;
    else return grid[y][x];
  }
  
    
    
  public int countNeighbors(int x,int y){
        int count=0;
        for (int i=-1; i<=1; i+=1){
            for(int j=-1; j<=1; j+=1){
                if (!(i==0 && j==0)){
                    count+=getSquare(x+i,y+j);
                }
            }
        }
        return count;
  }
  void displayGrid(){
        for(int rowI=0;rowI<grid.length;rowI++){
            for(int cellI=0;cellI<grid[rowI].length;cellI++){
                if(grid[rowI][cellI]==1)fill(0);
                else fill(255);
                rect(cellI*cellWidth,rowI*cellHeight,cellWidth,cellHeight);
            }
        }
  }
  int updateGrid(){
        int[][] newGrid=new int[gridHeight][];
        int aliveCount=0;
        for(int rowI=0;rowI<grid.length;rowI++){
            newGrid[rowI]=new int[gridWidth];
            for(int cellI=0;cellI<grid[rowI].length;cellI++){
                int neighbors=countNeighbors(cellI,rowI);
                int alive=0;
                if(neighbors<2)alive=0;
                else if(grid[rowI][cellI]==1 && neighbors<=3)alive=1;
                else if(neighbors==3) alive=1;
                else alive=0;
                newGrid[rowI][cellI]=alive;
                aliveCount+=alive;
            }
        
        }
        grid=newGrid;
        return(aliveCount);
  }
    void randomize(){
        for(int rowI=0;rowI<grid.length;rowI++){
            for(int cellI=0;cellI<grid[rowI].length;cellI++){
                grid[rowI][cellI]=(int)random(0,2);
            }
        }
    }
    void clear(){
        for(int rowI=0;rowI<grid.length;rowI++){
            for(int cellI=0;cellI<grid[rowI].length;cellI++){
                grid[rowI][cellI]=0;
            }
        }
    }
}

class Animal implements Comparable<Animal>{
    float [][] map;
    float fitness;
    int width,height;
    Grid animalGrid;
    Animal(int width,int height){
        this.width=width;
        this.height=height;
        map = new float[height][];
        fitness = 0;
        animalGrid =new Grid(width,height);
        for(int rowI=0;rowI<height;rowI++){
            map[rowI]=new float[width];
            for(int cellI=0;cellI<width;cellI++){
              map[rowI][cellI]=random(0,1);
            }
        }
    }

  
    void createGrid(){
       animalGrid = new Grid(width,height);
       for(int rowI=0;rowI<height;rowI++){
            for(int cellI=0;cellI<width;cellI++){
                if(map[rowI][cellI] > .95){//0.95
                    animalGrid.grid[rowI][cellI] = 1;
                }
            }
       }
    }

    float calculateFitness(int iterations){
      /**
        float total = 0.0;
        for(int i=0;i<iterations;i++){
            total += animalGrid.updateGrid();
        }

        //fitness=animalGrid.updateGrid();
        
        fitness = total/iterations;
        return fitness;
        **/
        for(int i=0;i<iterations;i++){
            fitness = animalGrid.updateGrid();
        }
        return fitness;
        
    }
    Animal breed(Animal other){
       Animal aOut = new Animal(width, height);


       for(int rowI=0;rowI<height;rowI++){
          for(int cellI=0;cellI<width;cellI++){
                if(random(1) > .5) aOut.map[rowI][cellI] = map[rowI][cellI];
                else aOut.map[rowI][cellI]= other.map[rowI][cellI];
                
                if(random(1)<mutationRate){//random mutation
                    aOut.map[rowI][cellI]=random(1);
                }
          }
       }
        return aOut;
    }
    public int compareTo(Animal other){
      if(fitness==other.fitness)return 0;
      if(fitness-other.fitness>0)return -1;
      else return 1;
      //return fitness-other.fitness;
    }
}





public Animal getRandom(Animal[] array) {
    int rnd = (int)random(array.length);
    return array[rnd];
}

Animal[] runGen(Animal[] generation){
    float tot = 0.0;
    for(int c=0;c<generation.length;c++){
        generation[c].createGrid();
        generation[c].calculateFitness(iterations);
        tot += generation[c].fitness;
    }
    Arrays.sort(generation);

    println((generation[0].fitness)+" "+(tot/(generation.length)));


    Animal[] parents=Arrays.copyOfRange(generation,0,parentCount);//get top performances
    
    
    Animal[] nextGen=new Animal[generation.length];
    
    
    System.arraycopy(generation,0,nextGen,0,keeperCount);//keep 5 best parents
    

    
    int addAt=keeperCount;
    for(int i=0;i<realChildren;i++){
          nextGen[addAt]=getRandom(parents).breed(getRandom(parents));
          nextGen[addAt].createGrid();
          addAt++;
        
    }
    while(addAt<generation.length){
        Animal newAnimal=new Animal(boardWidth,boardHeight);
        newAnimal.createGrid();
        nextGen[addAt]=(newAnimal);
        addAt++;
    }
    return nextGen;
}

int i;
Animal[] generation;

void setup() 
{
  output = createWriter("learning.txt"); 
  
  size(1000,500);
  frameRate(10000000);
  
  generation = new Animal[genSize];
  for(int c=0;c<generation.length;c++)generation[c] = new Animal(boardWidth,boardHeight);

  i=0;
  noStroke();

}


void draw() { 
  background(255);
  i++;
  if(i==iterations){
    i=0;
    generation=runGen(generation);
    generation[0].createGrid();
    history.add(generation[0].fitness);
    output.println(generation[0].fitness);
    output.flush(); // Writes the remaining data to the file
  }
  generation[0].animalGrid.updateGrid();
  generation[0].animalGrid.displayGrid();
  
  float spacing = 500/(history.size()+1.0);
  stroke(5);
  for(int i = 0; i < history.size()-1; i++){
    line(i*spacing+500, 500-history.get(i), (i+1)*spacing+500, 500-history.get(i+1));
  }
} 

void stop() {
  output.flush(); // Writes the remaining data to the file
  output.close(); // Finishes the file
}
