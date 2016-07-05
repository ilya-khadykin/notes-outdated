class Walker {
  int x;
  int y;
  
  Walker(){     // class constructor
   x = width/2;
   y = height/2; 
  }
  
  void display() {
    stroke(0);
    point(x,y);
  }
  
  void step() {
    float stepx = random(-1, 1); // random float number between -1.0 and 1.0
    float stepy = random(-1, 1);
    
    x += stepx;
    y += stepy;
  }
}

// processing code
void setup() {
  size(640,360);
  w = new Walker(); // create class instance
  background(255);
}
void draw() {
  w.step();
  w.display();
}



