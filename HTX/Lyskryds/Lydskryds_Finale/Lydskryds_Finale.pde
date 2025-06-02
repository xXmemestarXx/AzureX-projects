Trafik0 t1, t2, t3, t4;


void setup() {
  size (800, 800);

  // draw looper 60 gange og i vil ikke oprette variabler så mange gange. 
  //t1 og t3 beskriver lyskryds lodret hvor én er på højre nederst og den anden er venstre øverst, t2 og t4 er vandret og står venstre nederst og højre øverst
  t1 = new Trafik0(290, 230);
  t1.setState(0);

  t2 = new Trafik0(480, 230);
  t2.setState(8);
  
  t3 = new Trafik0(480,480);
  t3.setState(0);
  
  t4 = new Trafik0(290,480);
  t4.setState(8);
}
void draw() {
  background (255); // tagn forfra hver gang draw looper
  t1.drawTrafik0();
  t2.drawTrafik0();
  t3.drawTrafik0();
  t4.drawTrafik0();
  
  //Sorte veje
  fill(0);
  rect(350,0,100,800);
  fill(0);
  rect(0,350,800,100);
  
  //Lodret vej strej
  fill(255);
  rect(395,0,10,350);
  fill(255);
  rect(395,450,10,350);
  
  //Vandret vej strej
  fill(255);
  rect(0,395,350,10);
  fill(255);
  rect(450,395,350,10);
  
  //Stop streje
  fill(255);
  rect(345,350,5,100);
  fill(255);
  rect(450,350,5,100);
  fill(255);
  rect(350,345,100,5);
  fill(255);
  rect(350,450,100,5);
  

  print(t1.getState()+" ");
  println(t2.getState());

  if (t1.getState()<15) {
    t1.setState(t1.getState()+1);
  } else {
    t1.setState(0);
  }

  if (t2.getState()<15) { 
    t2.setState(t2.getState()+1);
  } else {
    t2.setState(0);
  }
  
  if (t3.getState()<15) { 
    t3.setState(t3.getState()+1);
  } else {
    t3.setState(0);
  }
  
  if (t4.getState()<15) { 
    t4.setState(t4.getState()+1);
  } else {
    t4.setState(0);
  }
  
  delay(1000);
  
}
