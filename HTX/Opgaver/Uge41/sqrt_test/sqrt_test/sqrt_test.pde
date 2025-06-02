float floaty = 2; 
float floaty2 = 2;
double doubles = 2;
double doubles2 = 2;

float a = sqrt(floaty);
float b = sqrt(floaty2);  
float c = a*b;
println(c);


double a1 = Math.sqrt(doubles);
double b1 = Math.sqrt(doubles2);
double c1 = a*b;
print(c1);

//Her ses der at der bruges langt flere decimaler ved double, altså det er mere eksakt. 
//Dog er det faktisk Math.sqrt der giver det flere decimaler,
//da den giver et output i double, så dette ville også virke med floats 
