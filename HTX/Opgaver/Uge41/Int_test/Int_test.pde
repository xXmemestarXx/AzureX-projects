//Int max er 2^31-1 til -2^31-1
//Her ses der at maksværdien er 2^32-1 til -2^31

boolean sand = true;

// variabel til test af integer datatypen, tallet starter højt, da maks værdien for et int er 2^31
int nummer = 2147480000;

void setup(){
    size(400,600); //Definere canvas størrelse
}

void draw(){
  background(225);
  // looper så længe den er sand.
  while(sand){
    // kald min funktion med værdien i nummer og læg resultatet tilbage i nummer
    nummer = testint(nummer);
    // skirv nummer til console
    println(nummer);
    
   if (nummer < 0){
   sand=false;
   }
  }
  

}
//Funktion der lægger 1 til tallet 
int testint(int x){
  return x+1;
}
