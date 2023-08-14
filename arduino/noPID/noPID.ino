#include <SoftwareSerial.h>

SoftwareSerial BTSerial(11,10); // RX, TX pins for Bluetooth module

#define L_MOTOR_POSITIVE 7
#define L_MOTOR_NEGATIVE 8
#define L_MOTOR_ENABLE 9
#define R_MOTOR_POSITIVE 2
#define R_MOTOR_NEGATIVE 4
#define R_MOTOR_ENABLE 5
#define LED_PIN 13
#define MAX_SPEED_R 200
#define MAX_SPEED_L 255

/*
 * Movements:
 *     W := forward
 *     S := stop
 *     D := right
 *     A := left
 *     R := extreme right
 *     L := extreme left
 *     X := reverse
 */

void setup() {
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  BTSerial.begin(9600);
}

String incomingByte;

void loop() {
  if (Serial.available() > 0) {
    incomingByte = BTSerial.readStringUntil(' ');

    Serial.println(incomingByte)

    if (incomingByte == 'A') {
      digitalWrite(L_MOTOR_POSITIVE, LOW);
      digitalWrite(L_MOTOR_NEGATIVE, LOW);

      digitalWrite(R_MOTOR_POSITIVE, LOW);
      digitalWrite(R_MOTOR_NEGATIVE, HIGH);

      analogWrite(L_MOTOR_ENABLE, MAX_SPEED_L);
      analogWrite(R_MOTOR_ENABLE, MAX_SPEED_R);
    }
    else if (incomingByte == 'D') {
      digitalWrite(L_MOTOR_POSITIVE, LOW);
      digitalWrite(L_MOTOR_NEGATIVE, HIGH);

      digitalWrite(R_MOTOR_POSITIVE, LOW);
      digitalWrite(R_MOTOR_NEGATIVE, LOW);

      analogWrite(L_MOTOR_ENABLE, MAX_SPEED_L);
      analogWrite(R_MOTOR_ENABLE, MAX_SPEED_R);
    }
    else if (incomingByte == 'W') {
      digitalWrite(L_MOTOR_POSITIVE, LOW);
      digitalWrite(L_MOTOR_NEGATIVE, HIGH);

      digitalWrite(R_MOTOR_POSITIVE, LOW);
      digitalWrite(R_MOTOR_NEGATIVE, HIGH);

      analogWrite(L_MOTOR_ENABLE, MAX_SPEED_L);
      analogWrite(R_MOTOR_ENABLE, MAX_SPEED_R);
    }
    
     
    else if (incomingByte == 'S') {
      digitalWrite(R_MOTOR_POSITIVE, LOW);
      digitalWrite(R_MOTOR_NEGATIVE, LOW);

      digitalWrite(L_MOTOR_POSITIVE, LOW);
      digitalWrite(L_MOTOR_POSITIVE, LOW);

      digitalWrite(13, HIGH);
      delay(1000);
      digitalWrite(13, LOW);
    }
  }
}