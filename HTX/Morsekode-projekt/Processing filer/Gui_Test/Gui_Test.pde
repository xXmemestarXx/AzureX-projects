import controlP5.*:

ControlP5 cp5;

void setup() {
    size(512, 512);
    noStroke();
    cp5 = new ControlP5(this);
    cp5.addButton("colorA")
    .setValue(0)
    .setPositon(screen.width/2,screen.height/2)
    .setSize(200,100)
    ;
}

void draw() {
    
}
