import controlP5.*;

ControlP5 cp5;
 
PFont font;

String s = "Lorem ipsum dolor sit amet" + "consectetur adipiscing elit, sed do eiusmod tempor";
color fontcolor = color(247,245,245);

void setup() {
  size(700,700);
  //fullScreen();
  font = createFont("Thames",32);
  
  cp5 = new ControlP5(this);
  
  cp5.addTextfield("")
     .setPosition(20,300)
     .setSize(200,40)
     .setFont(font)
     .setFocus(true)
     .setColor(fontcolor)
     .setColorBackground(#374874)
     ;
}

void draw() {
  background(55,72,116);
  fill(247,245,245);
  textFont(font);
  text(s,100,100);
}
