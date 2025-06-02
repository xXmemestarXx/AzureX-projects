//Interface del.
import controlP5.*; //Import af biblotek.

PImage tabel; //Initering af PImage, for at indlæse et billede.

ControlP5 cp5; //Initering af cp5.

controlP5.Button b; //Initering af forskellige objekter.
controlP5.Button b1;
controlP5.Button b2;
controlP5.Textarea info;
controlP5.Textarea info_morsekode; 
Textlabel Oversaettelse_side;
Textlabel title_info;

//Dekleration af variabler til GUI
float fontSize_menu = 32;
float fontSize_info = 64;
float fontSize_morsekode = 64;
color fontcolor = color(247, 245, 245); //Farve til font.
color backgroundcolor = color(55, 72, 116); //Farve til baggrunden
int Buttonsizex = 300;
int Buttonsizey = 100;
int Screensizex = 1920;
int Screensizey = 1080;
boolean show_tabel = false;
boolean show_morsekode = false;

//Morsekode del
StringDict inventory; //Dictionary til at opbevare alle oversættelser.
String test = " "; //String til test af user input.
String cur = " "; //String der gemmer nuværende input.
String result = " "; //String der gemmer nuværende sætning.
int l; //Int til bestemmelse af længden af en string.
boolean last = false; //Boolean til bestemmelse af backspace.
String information = "Tryk på vilkårligt bogstav eller tal fx. 'b' eller '2'. \n"
  +"Tryk '.' eller '-' for at danne morsekode \n"
  +"Tryk ENTER for at bekræfte valg \n"
  +"Tryk BACKSPACE for at slette tegn \n"
  +"Tryk SHIFT + 7 for at lave '/'";

String information2 = "Mellem 1837 og 1843 opfandt amerikaneren Samuel Morse morsekoden" //Sæt teksten til følgende.
  +"som brug til den elektriske telegraf. I 1847 får han patent på Beylerbeyi palads."
  +" Europa vedtog det som standard i 1851. Morsekode blev brugt som standard inden for"
  +"sø navigation helt op til 1999 hvor det blev erstattet af GMDSS."
  +" Den franske flåde gik bort fra morse i 1997 og deres sidste besked var:"
  +" Appel à tous. Ceci est notre dernier cri avant notre silence éternel." 
  +" Som betyder: 'Kald til alle. Dette er vores sidste råb før vores evige stilhed.' "
  +"Morsekode lever dog stadig videre i mange amatørradioer.";

void setup() {
  //Morsekode del
  inventory = new StringDict(); //Definere dictionariet ved navn inventory.
  //Fra alfabet til morse
  inventory.set(" ", "");
  inventory.set("  ", " ");
  inventory.set(" a", ".- ");
  inventory.set(" b", "-... ");
  inventory.set(" c", "-.-. ");
  inventory.set(" d", "-.. ");
  inventory.set(" e", ". ");
  inventory.set(" f", "..-. ");
  inventory.set(" g", "--. ");
  inventory.set(" h", ".... ");
  inventory.set(" i", ".. ");
  inventory.set(" j", ".--- ");
  inventory.set(" k", "-.- ");
  inventory.set(" l", ".-.. ");
  inventory.set(" m", "-- ");
  inventory.set(" n", "-. ");
  inventory.set(" o", "--- ");
  inventory.set(" p", ".--. ");
  inventory.set(" q", "--.- ");
  inventory.set(" r", ".-. ");
  inventory.set(" s", "... ");
  inventory.set(" t", "- ");
  inventory.set(" u", "..- ");
  inventory.set(" v", "...- ");
  inventory.set(" w", ".-- ");
  inventory.set(" x", "-..- ");
  inventory.set(" y", "-.-- ");
  inventory.set(" z", "--.. ");

  //Fra tal til morse
  inventory.set(" 1", ".---- ");
  inventory.set(" 2", "..--- ");
  inventory.set(" 3", "...-- ");
  inventory.set(" 4", "....- ");
  inventory.set(" 5", "..... ");
  inventory.set(" 6", "-.... ");
  inventory.set(" 7", "--... ");
  inventory.set(" 8", "---.. ");
  inventory.set(" 9", "----. ");
  inventory.set(" 0", "----- ");

  //Fra morse til tal
  inventory.set(" .----", "1");
  inventory.set(" ..---", "2");
  inventory.set(" ...--", "3");
  inventory.set(" ....-", "4");
  inventory.set(" .....", "5");
  inventory.set(" -....", "6");
  inventory.set(" --...", "7");
  inventory.set(" ---..", "8");
  inventory.set(" ----.", "9");
  inventory.set(" -----", "0");

  //Fra morse til alfabet
  inventory.set(" .-", "a");
  inventory.set(" -...", "b");
  inventory.set(" -.-.", "c");
  inventory.set(" -..", "d");
  inventory.set(" .", "e");
  inventory.set(" ..-.", "f");
  inventory.set(" --.", "g");
  inventory.set(" ....", "h");
  inventory.set(" ..", "i");
  inventory.set(" .---", "j");
  inventory.set(" -.-", "k");
  inventory.set(" .-..", "l");
  inventory.set(" --", "m");
  inventory.set(" -.", "n");
  inventory.set(" ---", "o");
  inventory.set(" .--.", "p");
  inventory.set(" --.-", "q");
  inventory.set(" .-.", "r");
  inventory.set(" ...", "s");
  inventory.set(" -", "t");
  inventory.set(" ..-", "u");
  inventory.set(" ...-", "v");
  inventory.set(" .--", "w");
  inventory.set(" -..-", "x");
  inventory.set(" -.--", "y");
  inventory.set(" --..", "z");

  PFont pfont = createFont("Thames", fontSize_menu, true); //Font håndtering med PFont.
  ControlFont font = new ControlFont(pfont, 32); //Font håndtering til cp5.

  PFont pfont1 = createFont("Thames", fontSize_info, true); //Font håndtering med PFont. 
  ControlFont font1 = new ControlFont(pfont1, 64); //Font håndtering til cp5.

  PFont pfont2 = createFont("Thames", 48, true);
  ControlFont font2 = new ControlFont(pfont2, 48);

  PFont pfont3 = createFont("Thames", fontSize_morsekode, true); //Font håndtering med PFont.

  fill(fontcolor); //Sætter farven på teksten til den valgte RGB værdi i variablen.
  textFont(pfont3); //Sætter tekst fonten til den valgte font.

  tabel = loadImage("tabel.jpg"); //Deklare en variable til hvilken fil der skal håndteres som billede.

  size(1920, 1080); //Sæt vindue størrelse
  smooth(); //Sæt teksten til at renderes som smooth (Glatter det ud).

  cp5 = new ControlP5(this); //Deklarering af cp5, ved at kalde kontruktøren "ControlP5" og referrer til sketchen selv.  

  b = cp5.addButton("Informations side") //Lav en knap.
    .setPosition((Screensizex/2-120)-Buttonsizex, Screensizey/2-Buttonsizey) //Sæt positionen af knappen.
    .setSize(Buttonsizex, Buttonsizey) //Sæt størrelsen af knappen.
    ;

  b1 = cp5.addButton("Oversættelses side") //Lav en knap.
    .setPosition((Screensizex/2+380)-Buttonsizex, Screensizey/2-Buttonsizey) //Sæt positionen af knappen.
    .setSize(Buttonsizex, Buttonsizey) //Sæt størrelsen af knappen.
    ;

  b2 = cp5.addButton("Back") //Lav en knap.
    .hide()
    .setPosition(40, 40) //Sæt positionen af knappen.
    .setSize(80, 80) //Sæt størrelsen af knappen.
    ;

  b.getCaptionLabel() //Tag fat i tekstfeltet på knappe "b".
    .setFont(font) //Sæt font.
    .toUpperCase(false) //Gør det til små bogstaver efter begyndelsesbogstav.
    .setText("Informations side") //Sæt teksten til feltet.
    .setColor(fontcolor) //Sæt farven på teksten.
    ;

  b1.getCaptionLabel() //Tag fat i tekstfeltet på knappe "b1".
    .setFont(font) 
    .toUpperCase(false)
    .setText("Oversættelse side")
    .setColor(fontcolor)
    ;

  b2.getCaptionLabel() //Tag fat i tekstfeltet på knappe "b2".
    .setFont(font)
    .toUpperCase(false)
    .setText("Back")
    .setColor(fontcolor)
    ;

  info = cp5.addTextarea("Information") //Lav tekstområde.
    .hide() //Skjul objektet
    .setPosition(380, 220) 
    .setSize(1200, 800)
    .setFont(font2)
    .setLineHeight(45) //Sæt linjeafstanden fra sætning til sætning.
    .setColor(fontcolor)
    .setColorBackground(backgroundcolor)
    .setText(information2)
    ;

  info_morsekode = cp5.addTextarea("How to") //Lav tekstområde.
    .hide()
    .setPosition(100, 200) 
    .setSize(800, 280)
    .setFont(font)
    .setLineHeight(45)
    .setColor(fontcolor)
    .setColorBackground(backgroundcolor)
    .setText(information);
  ;

  title_info = cp5.addTextlabel("title") //Lav title objekt.
    .hide()
    .setText("Informations Side")
    .setPosition(690, 100)
    .setColorValue(fontcolor) //Sæt farve på fonten.
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

void keyPressed () { //Initiering af keypressed funktion
  if (key == BACKSPACE) { //hvis knappen er backspace, reset current, hvis knappen er blevet trykket igen, slet en fra result
    cur = " ";
    if (last == true) {
      l = (result.length()) - 1;
      if (l>0) { 
        result = result.substring(0, l);
      }
    }
    last = true;
  } else if ((key == '.') || (key == '-')) { //Hvis knappen er '-' eller '.' så tilføj den til cur
    cur = cur + key;
    last = false;
  } else if (key == ENTER) { //Hvis knappen er ENTER, check om cur svarer til noget i inventory, hvis ja, tilføj til result, hvis nej, skriv fejl
    if (inventory.hasKey(cur) == true) {
      result = result + inventory.get(String.valueOf(cur));
      cur = " ";
    } else {
      cur = "#";
    }
    last = false;
  } else if (key == '/') { //Hvis knappen er '/', tilføj '/' til result
    result = result + '/'; 
    last = false;
  } else if (key == ' ') { //Hvis knappen er ' ', tilføj '' til result
    result = result + ' '; 
    last = false;
  } else { //Hvis knappen er noget andet, reset cur, test om knappen findes i inventory, hvis ja, tilføj til cur
    cur = " ";
    test = cur + key;
    if (inventory.hasKey(test) == true) {
      cur = cur + key;
    } 
    last = false;
  }
}

void controlEvent(ControlEvent TheEvent) { //Funktion der afventer en begivenhed.
  if (TheEvent.isFrom(cp5.getController("Informations side"))) { //Hvis der klikkes på knappen med navnet "Informations side".
    //Skjul og vis forskellige objekter.
    info.show();
    title_info.show();
    b2.show();
    b1.hide();
    b.hide();
    //Ændre de boolske værdi
    show_tabel = false;
    show_morsekode = false;
  }
  if (TheEvent.isFrom(cp5.getController("Oversættelses side"))) { //Hvis der klikkes på knappen med navnet "Oversættelses side".
    Oversaettelse_side.show();
    b2.show();
    b1.hide();
    b.hide();
    info_morsekode.show();
    show_tabel = true;
    show_morsekode = true;
  }
  if (TheEvent.isFrom(cp5.getController("Back"))) { //Hvis der klikkes på knappen med navnet "Back".
    Oversaettelse_side.hide();
    info.hide();
    title_info.hide();
    b2.hide();
    b1.show();
    b.show();
    info_morsekode.hide();
    show_tabel = false;
    show_morsekode = false;
  }
}

void draw() {
  background(backgroundcolor); //Sætter baggrund
  if (show_tabel == true) { //Hvis bool værdien er sand så indlæs billedet.
    image(tabel, 1000, 200);
  }
  if (show_morsekode == true) { //Hvis bool værdien er sand så skriv teksten.
    text(result, 100, height/2+60, 700, 700); //Angiv teksten, positionen og afgræns tekst området til de sidste 2 parameters værdier
    text(cur, 100, height/2);
  }
  if ((cur == " " || cur == "  ") && result == " " && show_morsekode == true) { //Hvis betingelserne er sande så skriv teksten
    text("Type here...", width/4-200, height/2);
  }
}
