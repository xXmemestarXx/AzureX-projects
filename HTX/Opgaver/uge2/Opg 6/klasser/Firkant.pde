class Firkant {
  // klassens attributter/ tilstand
  float x, y, s;  

  //konstroktøren
  Firkant() {
    this.x = random(400);
    this.y = random(600);
    this.s = random(300);
  }

  // klassens metoder
  
  // tegn firkant på canvas
  void drawFirkant() {
    square(x, y, s);
  }
}
