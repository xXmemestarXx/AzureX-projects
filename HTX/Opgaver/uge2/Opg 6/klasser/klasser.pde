// initiering af variablen f
Firkant f;
Cirkel c;
Trekant t;
Rektangel r;

int tal = int(random(2));

void setup() {
  size (600, 400);
  frameRate(10);
}

void draw() {
  // initiering af objektet f
  f = new Firkant();
  c = new Cirkel();
  t = new Trekant();
  r = new Rektangel();
  // tegner firkanten på canvas
  f.drawFirkant();
  c.drawCirkel();
  t.drawTrekant();
  r.drawRektangel();
}
