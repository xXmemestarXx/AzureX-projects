class Trekant {
  // klassens attributter/ tilstand
  float x, y, x2, y2, x3, y3;  

  //konstroktøren
  Trekant() {
    this.x = random(400);
    this.y = random(600);
    this.x2 = random(400);
    this.y2 = random(600);
    this.x3 = random(400);
    this.y3 = random(600);
  }

  // klassens metoder
  
  // tegn firkant på canvas
  void drawTrekant() {
    triangle(x, y, x2, y2, x3, y3);
  }
}
