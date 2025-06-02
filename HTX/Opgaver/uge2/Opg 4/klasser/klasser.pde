// initiering af variablen f
Firkant f;
Cirkel c;


void setup() {
  size (600, 400);
  frameRate(10);
}

void draw() {
  int tal = int(random(3));
  // initiering af objektet f
  f = new Firkant();
  c = new Cirkel();
  // tegner firkanten på canvas
  if(tal == 1){
  f.drawFirkant();
  }else{
  c.drawCirkel();
}
}
