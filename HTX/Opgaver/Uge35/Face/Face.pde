PShape Face; //<>//
float r;

void setup() {
size(400, 600);
Face = createShape(GROUP);

strokeWeight(1);
PShape Head = createShape(ELLIPSE,200,300,300,300);

strokeWeight(1);
fill(255);
PShape eyeleft = createShape(RECT, 125,225,50,50);
PShape eyeright = createShape(RECT, 225,225,50,50);

PShape Nose = createShape(ELLIPSE, 200, 300, 100, 100);

PShape Mouth = createShape(ARC,200,360,150,150,0,PI,CHORD);

fill(0);
strokeWeight(10);
PShape Hatbrim = createShape(RECT, 50,170,300,4, ROUND);
PShape Hat = createShape(RECT, 125,20,150,150);

Face.addChild(Head);
Face.addChild(eyeleft);
Face.addChild(eyeright);
Face.addChild(Nose);
Face.addChild(Mouth);
Face.addChild(Hat);
Face.addChild(Hatbrim);
}

void draw(){
 translate(width/2, height/2);
 background(204);

 r += 0.05;
 rotate(r);
 shape(Face, -width/2, -height/2);

}
