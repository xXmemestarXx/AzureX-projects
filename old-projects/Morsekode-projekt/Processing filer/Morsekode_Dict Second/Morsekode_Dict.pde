StringDict inventory;
String morsekode = ""; // variablre toil at gemme bogstaver
//ArrayList<String> morseliste = new ArrayList<String>();

void setup() {
  size(200, 200);
  inventory = new StringDict();
  //Fra alfabet til morse
  inventory.set(" ","   ");
  inventory.set("a",".-");
  inventory.set("b","-...");
  inventory.set("c","-.-.");
  inventory.set("d",".--");
  inventory.set("e",".");
  inventory.set("f","..-.");
  inventory.set("g","--.");
  inventory.set("h","...");
  inventory.set("i","..");
  inventory.set("j",".---");
  inventory.set("k",".--");
  inventory.set("l",".-..");
  inventory.set("m","--");
  inventory.set("n","-.");
  inventory.set("o","---");
  inventory.set("p",".--.");
  inventory.set("q","--.-");
  inventory.set("r",".-.");
  inventory.set("s","...");
  inventory.set("t","-");
  inventory.set("u","..-");
  inventory.set("v","...-");
  inventory.set("w",".--");
  inventory.set("x","-..-");
  inventory.set("y","-.--");
  inventory.set("z","--..");
  //Fra morse til alfabet
  inventory.set(".-","a");
  inventory.set("-...","b");
  inventory.set("-.-.","c");
  inventory.set(".--","d");
  inventory.set(".","e");
  inventory.set("..-.","f");
  inventory.set("--.","g");
  inventory.set("...","h");
  inventory.set("..","i");
  inventory.set(".---","j");
  inventory.set(".--","k");
  inventory.set(".-..","l");
  inventory.set("--","m");
  inventory.set("-.","n");
  inventory.set("---","o");
  inventory.set(".--.","p");
  inventory.set("--.-","q");
  inventory.set(".-.","r");
  inventory.set("...","s");
  inventory.set("-","t");
  inventory.set("..-","u");
  inventory.set("...-","v");
  inventory.set(".--","w");
  inventory.set("-..-","x");
  inventory.set("-.--","y");
  inventory.set("--..","z");
  
 // println(inventory);
  fill(0);
  textAlign(CENTER);
  textSize(20);
}

void keyPressed () {
  morsekode = inventory.get(String.valueOf(key));
 println(morsekode);
 
}

void draw() {
  /*String morsekode = inventory.get();
   morsekode = morsekode+inventory.get("B");
   morsekode = morsekode+inventory.get(" ");
   morsekode = morsekode+inventory.get("C"); */
   str.length(); 
   text(morsekode, width/2, height/2);
  
} 
