
  class Point {

  PVector loc;
  //PVector test;
  PVector pixelLoc;
  
  int label;
  float bias;


  Point() {
    loc = new PVector (random(-1, 1), random(-1, 1));
 
    Label();
  }
  Point (PVector setLoc) {
    loc = setLoc;
    Label();
  }

  void Label() {
     pixelLoc = scalePixel(loc);
    if(loc.y>f(loc.x)){
      label = 1;
    }
    else{
      label = -1;
    }
  }
  
  void show(){
    if(label ==1){
      fill(255);
    }
    else{
      fill(0);
    }
    stroke(0);
    ellipse(pixelLoc.x,pixelLoc.y,16,16);
  }
}