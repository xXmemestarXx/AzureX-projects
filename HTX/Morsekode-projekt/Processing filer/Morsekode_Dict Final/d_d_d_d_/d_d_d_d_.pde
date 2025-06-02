StringDict inventory;
String morsekode = ""; // variabler til at gemme bogstaver
//ArrayList<String> morseliste = new ArrayList<String>();
String test = " ";
String print = " ";
String cur = " ";
String result = " ";
int l;
boolean last = false;

void setup() {
  size(400, 400);
  inventory = new StringDict();
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

  // println(inventory);
  fill(0);
  textAlign(CENTER);
  textSize(20);
}


void keyPressed () {
  if (key == BACKSPACE) {
    cur = " ";
    if (last == true) {
      l = (result.length()) - 1;
      if (l>0) {
        result = result.substring(0, l);
      }
    }
    last = true;
  } else if ((key == '.') || (key == '-')  ) {
    cur = cur + key;
    last = false;
  } else if (key == ENTER) {
    if (inventory.hasKey(cur) == true) {
      result = result + inventory.get(String.valueOf(cur));
      cur = " ";
    } else {
      cur = "#";
    }
    last = false;
  } else if (key == '/') {
    result = result + '/'; 
    last = false;
  } else if (key == ' ') {
    result = result + ' '; 
    last = false;
  } else {
    cur = " ";
    test = cur + key;
    if (inventory.hasKey(test) == true) {
      cur = cur + key;
    } else {
      cur = " ";
    }
    last = false;
  }
}

void draw() {
  background(225);
  text(result, width/2, height/2+20);
  text(cur, width/2, height/2);
}
