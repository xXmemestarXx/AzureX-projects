// initiering af variablen f
Firkant f;
Cirkel c;
int tal = int(random(2));

void setup() {
  size (600, 400);
}

void draw() {
  // initiering af objektet f
  f = new Firkant();
  c = new Cirkel();
  // tegner firkanten på canvas
  f.drawFirkant();
  c.drawCirkel();
}
