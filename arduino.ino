
void setup() {
  Serial.begin(9600);
  pinMode(5, OUTPUT);  //5 should be replaced by your own LED pin
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    if (cmd == '1') {
      digitalWrite(5, HIGH);  
    } else if (cmd == '0') {
      digitalWrite(5, LOW);   
    }
  }
}
