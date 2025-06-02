class Firkant {
  // klassens attributter/ tilstand
  float x, y;
  int r = int(random(256));
  int g = int(random(256));
  int b = int(random(256));
  //konstroktøren
  Firkant() {
    this.x = random(400);
    this.y = random(600);
  }

  // klassens metoder
  
  // tegn firkant på canvas
  void drawFirkant() {
    fill(r,g,b);
    circle(x, y, 100);
  }
}
