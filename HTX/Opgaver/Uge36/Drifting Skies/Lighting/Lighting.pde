PShape lightning;

void setup(){
size(1000, 600);
fill(235, 213, 52);
lightning = createShape();
lightning.beginShape();
lightning.vertex(279.48, 270.84);
lightning.vertex(309.69, 364.1);
lightning.vertex(125.79, 340.46);
lightning.vertex(418.72, 520.42);
lightning.vertex(400, 400);
lightning.vertex(535.63, 445.55);
lightning.vertex(500, 300);
lightning.endShape();
}

void draw(){
background(52);
shape(lightning);

}
