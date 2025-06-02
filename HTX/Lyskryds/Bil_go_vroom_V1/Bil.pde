class Bil {
  //int speed;
  //float xpos;
  //float ypos;
  int id;
  PVector location;
  PVector velocity;
  int r = (int)random(256);
  int g = (int)random(256);
  int b = (int)random(256);

  //konstruktør
  Bil(int speed, float xpos, float ypos, int id) {
    //this.speed=speed;
    velocity = new PVector(speed, 0);
    location = new PVector(xpos, ypos);
    this.id=id;
  }
  float getspeed() {
    //return this.speed;
    return velocity.x;
  }
  void setspeed(float speed) {
    //this.speed=speed;
    // tvinger værdien til at være mellem 1 og 10
    this.velocity.x=constrain(speed, 0, 5);
  }
  float getxpos() {
    //return this.xpos;
    return this.location.x;
  }
  void setxpos(float xpos) {
    //this.xpos=xpos;
    this.location.x=xpos;
  }
  float getypos() {
    //return this.ypos;
    return this.location.y;
  }
  void setypos(float ypos) {
    //this.ypos=ypos;
    this.location.y=ypos;
  }
  void displayBil() {
    fill(r, b, g);
    rect(location.x, location.y, 32, 16);
  }
  
  void displayBilhv() {
    pushMatrix();
    //translate(xpos*speed, 8*52);
    translate(location.x, 8*52);
    fill(r, b, g);
    rect(0, 0, 32, 16);
    popMatrix();
  }
  void displayBilvv() {
    pushMatrix();
    //translate(xpos*speed, 8*48);
    translate(location.x, 8*48);
    fill(255);
    rect(800, 0, 32, 16);
    popMatrix();
  }
  void displayBilln() {
    pushMatrix();
    //translate(8*48, ypos*speed);
    translate(8*48, location.y);
    fill(255);
    rect(0, 0, 16, 32);
    popMatrix();
  }
  void displayBillo() {
    pushMatrix();
    //translate(8*52, ypos*speed);
    translate(8*52, location.y);
    fill(255);
    rect(0, 800, 16, 32);
    popMatrix();
  }

  void move() {
    this.location = this.location.add(this.velocity);
    if (location.x > width) {
      location.x = 0;
    } else if (location.x < 0) {
      location.x = width;
    }

    if (location.y > height) {
      location.y = 0;
    } else if (location.y < 0) {
      location.y = height;
    }
  }

  void checkCollision(Bil other) {
    //https://processing.org/examples/circlecollision.html

    float minDistance = 60.0f;
    // Get distances between the balls components
    PVector distanceVect = PVector.sub(other.location, location);

    // Calculate magnitude of the vector separating the balls
    float distanceVectMag = distanceVect.mag();
    

    if (distanceVectMag < minDistance && this.location.x < other.location.x) {
      this.setspeed(0);
      //println(id+" Stopper "+distanceVectMag+" "+minDistance+" "+this.velocity);
    }
    else if (distanceVectMag > minDistance && this.location.x > other.location.x) {
      this.setspeed(this.getspeed()+1);
      //println(id+" Gi gas "+distanceVectMag+" "+getspeed());
    }
    
    
  }
}
