
int LEDPIN=8;
int BUTTON1=7;


void setup() {
  // put your setup code here, to run once:
  pinMode(LEDPIN,INPUT);
  Serial.begin(9600); 

}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(BUTTON1)== LOW)
    digitalWrite(LEDPIN, HIGH);
  else
      digitalWrite(LEDPIN, LOW);
}
