import controlP5.*; //Import af libary

ControlP5 cp5; //init af cp5 

controlP5.Textarea info;

float fontSize = 64;

color fontcolor = color(247, 245, 245); //Farve til font
int Buttonsizex = 300;
int Buttonsizey = 100;
int Screensizex = 1920;
int Screensizey = 1080;

void setup() {
  size(1920, 1080);
  cp5 = new ControlP5(this);
  
  info = cp5.addTextarea("txt")
  .setPosition(348,200)
  .setSize(1200,800)
  .setFont(createFont("Thames",48,true))
  .setLineHeight(45)
  .setColor(fontcolor)
  .setColorBackground(color(55, 72, 116))
  .setText("Lorem Ipsum is simply dummy text of the printing and typesetting"
           +" industry. Lorem Ipsum has been the industry's standard dummy text"
           +" ever since the 1500s, when an unknown printer took a galley of type"
           +" and scrambled it to make a type specimen book. It has survived not"
           +" only five centuries, but also the leap into electronic typesetting,"
           +" remaining essentially unchanged. It was popularised in the 1960s"
           +" with the release of Letraset sheets containing Lorem Ipsum passages,"
           +" and more recently with desktop publishing software like Aldus"
           +" PageMaker including versions of Lorem Ipsum."
           );
}

void draw() {
  PFont pfont = createFont("Thames", fontSize, true); //Font håndtering 
  ControlFont font = new ControlFont(pfont, 64);
  background(55, 72, 116); //Sætter baggrund
  text("Informations side", 730, 100);
  textFont(pfont);
  fill(255);
}
