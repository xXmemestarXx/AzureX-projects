import controlP5.*; //Import af libary

PImage tabel;

ControlP5 cp5; //init af cp5 

controlP5.Button b;
controlP5.Button b1;
controlP5.Button b2;
controlP5.Textarea info;
Textlabel Oversaettelse_side;
Textlabel title_info;

float fontSize_menu = 32;
float fontSize_info = 64;

color fontcolor = color(247, 245, 245); //Farve til font
int Buttonsizex = 300;
int Buttonsizey = 100;
int Screensizex = 1920;
int Screensizey = 1080;

boolean show_tabel = false;


void setup() {
  tabel = loadImage("tabel2.jpg");
  
  PFont pfont = createFont("Thames", fontSize_menu, true); //Font håndtering 
  ControlFont font = new ControlFont(pfont, 32);

  PFont pfont1 = createFont("Thames", fontSize_info, true); //Font håndtering 
  ControlFont font1 = new ControlFont(pfont, 64);

  size(1920, 1080);
  smooth();

  cp5 = new ControlP5(this);

  b = cp5.addButton("Informations side")
    .setPosition((Screensizex/2-120)-Buttonsizex, Screensizey/2-Buttonsizey)
    .setSize(Buttonsizex, Buttonsizey)
    .setLabel("Informations side")
    .setId(1)
    ;

  b1 = cp5.addButton("Oversættelses side") //Lav knap
    .setPosition((Screensizex/2+380)-Buttonsizex, Screensizey/2-Buttonsizey) //Sæt position
    .setSize(Buttonsizex, Buttonsizey) //Sæt størrelse
    .setLabel("Oversættelses side") //Giv label, til senere identification i logikken
    .setId(2)
    ;
    
  b2 = cp5.addButton("Back")
     .setPosition(40,40)
     .setSize(80, 80)
     .setLabel("Back")
     .setId(3)
     ;

  b.getCaptionLabel()
    .setFont(font)
    .toUpperCase(false)
    .setText("Informations side")
    .setColor(fontcolor)
    ;

  cp5.getController("Informations side")
    .getCaptionLabel()
    ;

  b1.getCaptionLabel()
    .setFont(font)
    .toUpperCase(false)
    .setText("Oversættelse side")
    .setColor(fontcolor)
    ;
    
  b2.getCaptionLabel()
    .setFont(font)
    .toUpperCase(false)
    .setText("Back")
    .setColor(fontcolor)
    ;

  info = cp5.addTextarea("txt")
    .hide()
    .setPosition(20, 200)
    .setSize(800, 800)
    .setFont(createFont("Thames", 48, true))
    .setLineHeight(45)
    .setColor(fontcolor)
    .setColorBackground(color(55, 72, 116))
    .setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit."
             +"Praesent pellentesque leo et augue sodales, eu semper nunc convallis."
             +"Quisque pharetra velit quis mollis tincidunt. Sed a magna volutpat," 
             +"ultrices sapien non, porta leo. Sed lobortis libero sed bibendum commodo." 
             +"In vel aliquet massa. Fusce sit amet tortor et nisl pulvinar rutrum et sed quam." 
             +"Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas."
    );

  title_info = cp5.addTextlabel("title")
    .hide()
    .setText("Informations Side")
    .setPosition(690, 100)
    .setColorValue(fontcolor)
    .setFont(font1)
    ;
    
  Oversaettelse_side = cp5.addTextlabel("title2")
    .hide()
    .setText("Oversættelse side")
    .setPosition(690, 100)
    .setColorValue(fontcolor)
    .setFont(font1)
    ;
}

void draw() {
  background(55, 72, 116); //Sætter baggrund
  if (show_tabel == true) {
    image(tabel, 1000, 200);
  }
}

void controlEvent(ControlEvent TheEvent) {
  if (TheEvent.isFrom(cp5.getController("Informations side"))) {
    info.show();
    title_info.show();
    b1.hide();
    b.hide();
    show_tabel = false;
  }
  if (TheEvent.isFrom(cp5.getController("Oversættelses side"))) {
    Oversaettelse_side.show();
    b1.hide();
    b.hide();
    show_tabel = true;
   }
   if (TheEvent.isFrom(cp5.getController("Back"))) {
    Oversaettelse_side.hide();
    info.hide();
    title_info.hide();
    b1.show();
    b.show();
    show_tabel = false;
}
}
