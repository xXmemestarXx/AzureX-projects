class Firkant {
  // klassens attributter/ tilstand
  float x, y;  

  //konstroktøren
  Firkant() {
    this.x = random(400);
    this.y = random(600);
  }

  // klassens metoder
  
  // tegn firkant på canvas
  void drawFirkant() {
    square(x, y, 100);
  }
}
