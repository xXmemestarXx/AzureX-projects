class Rektangel {
  // klassens attributter/ tilstand
  float x, y, x2, y2;  

  //konstroktøren
  Rektangel() {
    this.x = random(400);
    this.y = random(600);
    this.x2 = random(400);
    this.y2 = random(600);
  }

  // klassens metoder
  
  // tegn firkant på canvas
  void drawRektangel() {
    rect(x, y, x2, y2);
  }
}
