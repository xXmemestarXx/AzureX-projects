int belobUdenMoms = 100;
float belobMedMoms = 0;
String navn = "Bonde";
String adresse = "Vestergade 45"; 

void setup(){
  noLoop();
}

void draw(){
  float belobMedMoms = beregnMoms(belobUdenMoms);
  println("Beløb total:");
  println(belobMedMoms);
  println(" ");
  println("Beløb uden moms:");
  println(belobUdenMoms);
  println(" ");
  println(" ");
  println(day(),"/",month(),year(),hour(),":",minute());
  println(adresse);
  println("Du er blevet bejent af: " + navn);
}


float beregnMoms(int belob){
  return belob*1.25;
}
