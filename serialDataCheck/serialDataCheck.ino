#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10, 11); // RX, TX pins for Bluetooth module

void setup() {
    Serial.begin(9600);
    BTSerial.begin(9600);
}

void loop() {
    if (BTSerial.available()) {
        String receivedData = BTSerial.readStringUntil('\n'); // Read until newline character
        Serial.print("Received float: ");
        Serial.println(receivedData);
    }
}