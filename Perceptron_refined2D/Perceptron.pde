class Perceptron {
  float[] weights;
  float learningRate;
  Perceptron(int n,float lr) {
    weights = new float[n];
    learningRate=lr;
    for (int i = 0; i<weights.length; i++) {
      weights[i] = random(-1, 1);
    }
  }
  int guess(float[] inputs) {
    float sum = 0;
    for (int i=0; i<weights.length; i++) {
      sum+=inputs[i]*weights[i];
    }
    int output = activation(sum);
    return output;
  }

  void train(float[] inputs, int target) {
    int guess = guess(inputs);
    int error = target - guess;

    for (int i=0; i<weights.length; i++) {
      weights[i]+= error*inputs[i]*learningRate;
    }
  }
  
  float guessY( float x ) {
    return ((-1*weights[0])/weights[1]) * x - (weights[2]/weights[1]);
  }
}