class Cirkel {
  // klassens attributter/ tilstand
  float x, y, s;  

  //konstroktøren
  Cirkel() {
    this.x = random(400);
    this.y = random(600);
    this.s = random(101);
  }

  // klassens metoder
  
  // tegn firkant på canvas
  void drawCirkel() {
    circle(x, y, s);
  }
}
