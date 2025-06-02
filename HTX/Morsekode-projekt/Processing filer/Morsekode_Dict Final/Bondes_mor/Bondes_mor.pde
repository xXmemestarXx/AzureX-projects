StringDict inventory;
String morsekode = ""; // variabler til at gemme bogstaver
//ArrayList<String> morseliste = new ArrayList<String>();
String test = " ";
String print = " ";
String cur = " ";
String result = " ";

void setup() {
  size(400, 400);
  inventory = new StringDict();
  //Fra alfabet til morse
  inventory.set(" ", "   ");
  inventory.set("a", ".-");
  inventory.set("b", "-...");
  inventory.set("c", "-.-.");
  inventory.set("d", ".--");
  inventory.set("e", ".");
  inventory.set("f", "..-.");
  inventory.set("g", "--.");
  inventory.set("h", "...");
  inventory.set("i", "..");
  inventory.set("j", ".---");
  inventory.set("k", ".--");
  inventory.set("l", ".-..");
  inventory.set("m", "--");
  inventory.set("n", "-.");
  inventory.set("o", "---");
  inventory.set("p", ".--.");
  inventory.set("q", "--.-");
  inventory.set("r", ".-.");
  inventory.set("s", "...");
  inventory.set("t", "-");
  inventory.set("u", "..-");
  inventory.set("v", "...-");
  inventory.set("w", ".--");
  inventory.set("x", "-..-");
  inventory.set("y", "-.--");
  inventory.set("z", "--..");
  //Fra morse til alfabet
  inventory.set(" .-", "a");
  inventory.set(" -...", "b");
  inventory.set(" -.-.", "c");
  inventory.set(" .--", "d");
  inventory.set(" .", "e");
  inventory.set(" ..-.", "f");
  inventory.set(" --.", "g");
  inventory.set(" ...", "h");
  inventory.set(" ..", "i");
  inventory.set(" .---", "j");
  inventory.set(" .--", "k");
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

  // println(inventory);
  fill(0);
  textAlign(CENTER);
  textSize(20);
}


void keyPressed () {
  if (key == BACKSPACE) {
    result = " ";
  } else if ((key == '.') || (key == '-')  ) {
    test = cur + key;
    if (inventory.hasKey(test) == true) {
      cur = cur + key;
    }
    else {
     cur = " "; 
    }
    
  } else if (key == ',') {
    result = result + inventory.get(String.valueOf(cur));
    cur = " ";
  }
}

void draw() {
  background(225);
  /*String morsekode = inventory.get();
   morsekode = morsekode+inventory.get("B");
   morsekode = morsekode+inventory.get(" ");
   morsekode = morsekode+inventory.get("C"); */
  morsekode = inventory.get(String.valueOf(key));
  print = inventory.get(String.valueOf(cur));
  text(result, width/2, height/2+20);
  text(print, width/2, height/2);
}
