PShape s;

void setup() {
  size(800,800);
  s = createShape(RECT, 400, 400, 10, 10);
}

void draw() {
  background(204);
  shape(s);
}

void mousePressed() {
  // Rotate the shape each time the mouse is pressed
  s.rotate(0.1);  
}
