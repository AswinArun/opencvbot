#include <SoftwareSerial.h>

SoftwareSerial BTSerial(11,10); // RX, TX pins for Bluetooth module

const int enA = 9;
const int in1 = 8;
const int in2 = 7;
const int enB = 5;
const int in3 = 4;
const int in4 = 2;

const int led = 13;

float Kp = 1; // Proportional gain
float Ki = 0; // Integral gain
float Kd = 0.5; // Derivative gain
float integralError = 0;
float derivativeError = 0;

float prevError = 0;

float error = 0.0;
int basespeed = 0;

void setup() {
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
    
  Serial.begin(9600);
  BTSerial.begin(9600);
}

void loop() {
  if (BTSerial.available()) {
        error = (BTSerial.readStringUntil(' ')).toFloat(); // Read until newline  character


      /*if (error == 10){ //triangle obstacle
      digitalWrite(led, HIGH);
      delay(100);
      digitalWrite(led, LOW);
      continue;
    }

    else if (error == 20){ // rectangle obstacle
      digitalWrite(led, HIGH);
      delay(100);
      digitalWrite(led, LOW);
      delay(100);
      digitalWrite(led, HIGH);
      delay(100);
      digitalWrite(led, LOW);
      continue;
    }*/

    // Print LDR values for debugging
    Serial.println(error);

    integralError+= error;

    derivativeError = error - prevError;


    prevError = error;

    // Calculate control signals for left and right motors
    int controlSignal = Kp * error + Ki * integralError + Kd * derivativeError;
    // Clip the control signals to avoid excessive values
    controlSignal = constrain(controlSignal, -255, 255);
    applyMotorControl(controlSignal);
    //Serial.println(controlSignal);
  }
  
  
}

void applyMotorControl(int controlSignal) {
  //if (controlSignal >= 0) {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    analogWrite(enA, 255 );

    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
    analogWrite(enB, 255 );
  /*} else {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    analogWrite(enA, basespeed - controlSignal);

    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    analogWrite(enB, basespeed + controlSignal);
  }*/
}