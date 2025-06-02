// initiering af variablen f
Firkant f;

void setup() {
  size (600, 400);
}

void draw() {
  // initiering af objektet f
  f = new Firkant();
  // tegner firkanten på canvas
  f.drawFirkant();
}
