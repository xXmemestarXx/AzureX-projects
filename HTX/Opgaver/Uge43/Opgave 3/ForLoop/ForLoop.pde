int i;
String s = "Dette er en sætning som indeholder mange e'er. Men hvor mange er der?";
char achar;
int x = 0;

for (i=0; i<s.length(); i++) {
  achar = s.charAt(i);
  if (achar == 'e') {
    println(achar);
    x++;
  }
  if (i == s.length()-1) {
    println(x);
  }
}
