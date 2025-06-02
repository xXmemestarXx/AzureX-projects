float r; 
void setup(){
  size(700, 600);
}

void draw(){
  background(0, 0, 255);
  drawLandscape();
  translate(0+r, 0);
  r += 0.8;
  if(r>200){
    r=0;
  }

  for (int i = 0; i < width+200; i++) {
   if(i %  200==0) {
    drawClouds(i-200, 0);
    drawClouds(i-150, 150);
   }
  }
}

void drawLandscape(){
  fill(0, 225, 0);
  stroke(0, 225, 0);
  circle(100, 900, 800);
  circle(600, 900, 800);
}

void drawClouds(int x, int y) {
  fill(204);
  stroke(255);
  circle(x, y, 75);
  circle(x+25, y-30, 70);
  circle(x+25, y+30, 70);
  circle(x+50, y-30, 70);
  circle(x+50, y+30, 70);
  circle(x+75, y, 70);
}
