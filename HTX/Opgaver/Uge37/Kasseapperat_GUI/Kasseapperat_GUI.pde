int belobUdenMoms = 100;
int belobMedMoms = 0;
int widthbon = 260;
int lengthbon = 660;
String firma = "Bonde A/S";
String adresse = "Adresse: Vestergade 45"; 
String navn = "Bonde";
int day = day();
int month = month();
int year = year();
int hour = hour();
int minutes = minute();

void setup(){
size(300, 700);
rect(20, 20, widthbon, lengthbon);
}

void draw(){
Kassedelen();
Title();
Info();
}

void Title(){
translate(60, 40);
textSize(18);
text(firma, widthbon/2, 20);
}

void Info(){
textAlign(RIGHT);
textSize(12);
fill(0);
translate(80, 50);
text(adresse, 27, 0);
text("Du er blevet bejent af: " + navn, 57, 15);
text("dd/mm/yy: " + day, -33, 30);
text(month, -15, 30);
text(year, 20, 30);
}

void Kassedelen(){
textAlign(RIGHT);
textSize(15);
fill(0);
float belobMedMoms = beregnMoms(belobUdenMoms);
text("Beløb total:", 110, 200);
text(belobMedMoms, 175, 200);
text("Beløb uden moms:", 162, 220);
text(belobUdenMoms, 197, 220);
}

float beregnMoms(int belob){
  return belob*1.25;
}
