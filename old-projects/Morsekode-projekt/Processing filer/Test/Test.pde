import controlP5.*;

ControlP5 cp5;

void setup() {
    size(400,600);
    noStroke();
    cp5 = new ControlP5(this);

    cp5.addButton("Text1")
    .setValue(0)
    .setPosition(106,106)
    .setSize(200,30)
    ;
}

void draw() {
    background(69);
}
