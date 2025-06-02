int CarCount = 12;
Trafik0  t2, t4;
int i=0;

Bil[] bilListe = new Bil[CarCount];

void setup() {
  size(1600, 800);
  rectMode(CENTER);
  for (int i=0; i<bilListe.length; i++) {
    bilListe[i]=new Bil((int)random(1, 6), random(width), height/2+25, i);
  }
  /*t1 = new Trafik0(290, 230);
   t1.setState(0);*/

  t2 = new Trafik0(width/2+50, height/2-100);
  t2.setState(8);

  /*t3 = new Trafik0(480,480);
   t3.setState(0);*/

  t4 = new Trafik0(width/2-50, height/2+100);
  t4.setState(8);
}
void draw() {
  background(225);
  drawRoads();

  if (frameCount%60==0) { // skift en state i trafiklyset hvert sekund
    changeLght();
  }

  //t1.drawTrafik0();
  t2.drawTrafik0();
  //t3.drawTrafik0();
  t4.drawTrafik0();


  for (int i=0; i<bilListe.length; i++) {
    for (int j=0; j<bilListe.length; j++) {
      bilListe[i].checkCollision(bilListe[j]);
    }
    if (bilListe[i].getspeed()==0) {
      bilListe[i].setspeed(1);
    }
    println (t2.getState());
    println(t2.getDistToLight(bilListe[i].location));
    if (t2.getDistToLight(Bil)<50){// det er her jeg prover bare at få printet en line når bilen kommer tæt nok på lyskrydset men det gider ikke at virke. har prøvet mange forskellige muligheder end bare det her.
     println("stop bil"); 
    }
    // stopBil(); jeg prøvede også at lave en void funktion som tjekkede og stoppede bilen, dn virkede heller ikke
    //*********************************************
    // hvis (t2 er rød (state 6 til og med 15) og distancen til krydset er mindre en 100 t2.getDistToLight(bil) og noget mere
    // SÅ Standsbilen 
    //********************************************************************************************************
  }
  bilListe[i].move();
  bilListe[i].displayBil();
}  

/*void stopBil(){ //her er den void funktion som jeg prøvede at lave men fejlede med.
 if (t2.getState()>=6&&t2.getState()<=15&&t2.getDistToLight(bilListe[i].location)<50) {
    
        bilListe[i].setspeed(0);
      } else {
        bilListe[i].setspeed((float)random(1, 6));
      }
    } */


void drawRoads() {

  //Sorte veje
  rectMode(CORNER);
  fill(0);
  rect(0, height/2-50, width, 100);

  //Vandret vej strej
  fill(255);
  rect(0, 395, width, 10);

  //Stop streje
  rect(width/2-50, height/2-50, 5, 100);
  rect(width/2+50, height/2-50, 5, 100);

  rectMode(CENTER);
}

void changeLght() {
  //print(t1.getState()+" ");
  //println(t2.getState());

  /*if (t1.getState()<15) {
   t1.setState(t1.getState()+1);
   } else {
   t1.setState(0);
   }*/

  if (t2.getState()<15) { 
    t2.setState(t2.getState()+1);
  } else {
    t2.setState(0);
  }

  /*if (t3.getState()<15) { 
   t3.setState(t3.getState()+1);
   } else {
   t3.setState(0);
   }*/

  if (t4.getState()<15) { 
    t4.setState(t4.getState()+1);
  } else {
    t4.setState(0);
  }
}
