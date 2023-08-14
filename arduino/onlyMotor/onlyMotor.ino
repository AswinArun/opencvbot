const int enA = 9;
const int in1 = 8;
const int in2 = 7;
const int enB = 5;
const int in3 = 4;
const int in4 = 2;


void setup() {
  // put your setup code here, to run once:

  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);  //forward
  analogWrite(enA, 255);

  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enB, 255);
    
}
