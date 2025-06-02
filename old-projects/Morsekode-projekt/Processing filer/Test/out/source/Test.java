import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import controlP5.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class Test extends PApplet {



ControlP5 cp5;

public void setup() {
    
    noStroke();
    cp5 = new ControlP5(this);

    cp5.addButton("Text1")
    .setValue(0)
    .setPosition(106,106)
    .setSize(200,30)
    ;
}

public void draw() {
    background(69);
}
  public void settings() {  size(400,600); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Test" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
