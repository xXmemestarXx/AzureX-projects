import processing.sound.*;
SinOsc sine;

void setup() {
  size(640, 360);
  background(255);
    
  // Create the sine oscillator.
  sine = new SinOsc(this);  
}

void draw() {
  //the image is just for informative purposes
  //on how the soundwave looks
  
  
}

void keyPressed(){
  if(key == '.' || key == ':'){
      Short();
      }
      else if(key == '-' || key == '_') {
      Long();
      }
}
void Short() {
  sine.play();
  delay(100);
  sine.stop();
  delay(40);
}

void Long() {
  sine.play();
  delay(300);
  sine.stop();
    delay(40);
}
