
void setup() {
  Serial.begin(9600);
  pinMode(5, OUTPUT); #'5' should be replaced with your own pin
}

void loop() {
  if (Serial.available() > 0) {
    byte receivedByte = Serial.read(); 
    int receivedNumber = (int)receivedByte;
    int pwmValue = map(receivedNumber, 0, 100, 0, 255);
      analogWrite(5, pwmValue);
    }
  }
