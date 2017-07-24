float f(float x) {
  return -0.3*x +0.2;
}

PVector scalePixel(PVector location){
    return new PVector(map(location.x,-1,1,0,width),map(location.y,-1,1,height,0));
}

void drawActual(){
  Point p1 = new Point(new PVector(-1,f(-1)));
  Point p2 = new Point(new PVector(1,f(1)));
  line(p1.pixelLoc.x,p1.pixelLoc.y,p2.pixelLoc.x,p2.pixelLoc.y);
}

void drawlearnedLine(){
  Point p3 = new Point(new PVector(-1,brain.guessY(-1)));
  Point p4 = new Point(new PVector(1,brain.guessY(1)));
  line(p3.pixelLoc.x,p3.pixelLoc.y,p4.pixelLoc.x,p4.pixelLoc.y);
}

void initializePoints(int npoints){
  points = new Point[npoints];
  for(int i=0;i<points.length;i++){
    points[i]=new Point();
  }
}

void showPoints_Actual(){
  for(Point pt : points){
    pt.show();
  }
}

int activation(float n) {
  if (n>=0) {
    return 1;
  } else {
    return -1;
  }
}