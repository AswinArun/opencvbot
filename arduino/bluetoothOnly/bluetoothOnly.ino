#include<SoftwareSerial.h>

SoftwareSerial BTSerial(10,11);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  BTSerial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(BTSerial.available()) {
    float data = (BTSerial.readStringUntil(' ')).toFloat();
    Serial.println(data);
  }
}
