int CarCount = 12;

Bil[] bilListe = new Bil[CarCount];

void setup() {
  size(1600, 800);
  rectMode(CENTER);
  for(int i=0;i<bilListe.length;i++){
    bilListe[i]=new Bil((int)random(1,6), random(width), 0.0f,i);
  }
    
}
void draw() {
  background(225);
 
  for(int i=0;i<bilListe.length;i++){
    for(int j=0;j<bilListe.length;j++){
      bilListe[i].checkCollision(bilListe[j]);
    }
    if(bilListe[i].getspeed()==0){
      bilListe[i].setspeed(1);
    }
    bilListe[i].move();
    bilListe[i].displayBilhv();
    
  }  
}
