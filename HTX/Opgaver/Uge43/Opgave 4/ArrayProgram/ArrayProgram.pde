String s = "Løkken skal udskrive alle e'er og tilsidst udskrive hvor mange e'er som er fundet. Ja, så er det rigtigt :)";
int numbers[] = {39,19,41,6,4,16,6,16,35,99,41,48,99};
char achar;

for(int i=0;i<14;i++){
  achar = s.charAt(numbers[i]);
  print(achar);
}
  
