Perceptron brain;
Point[] points;
int trainingIndex =0;
int ndata=100;
void setup() {
  brain = new Perceptron(3, 0.01);
  size(700, 700);
  initializePoints(ndata);
}

void draw() {
  background(255);
  stroke(0);
  drawActual();
  showPoints_Actual();
  for (Point pt : points) {
    float[] inputs = {pt.loc.x, pt.loc.y, pt.bias};
    int target = pt.label;
    int guess = brain.guess(inputs);
    //brain.train(inputs, target);
    if (guess == target) {
      fill(0, 255, 0);
    } else {
      fill(255, 0, 0);
    }
    noStroke();
    ellipse(pt.pixelLoc.x, pt.pixelLoc.y, 8, 8);
  }
    Point train = points[trainingIndex];
  int target = train.label;
  float[] inputs = {train.loc.x, train.loc.y,train.bias};
  int guess = brain.guess(inputs);
  brain.train(inputs, target);
  trainingIndex = (trainingIndex+1) % points.length ;

  stroke(255,0,255);
  drawlearnedLine();
}