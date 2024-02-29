const int touchPin = 2;  // Pin where the touch sensor is connected
const int ledPin = 13;   // Pin where the LED is connected

int touchCount = 0;      // Variable to keep track of the number of touches

void setup() {
  pinMode(touchPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Read the touch sensor state
  int touchState = digitalRead(touchPin);
  char letter = Serial.read();

  // Check if the touch sensor is touched
  if (touchState == HIGH) {
    delay(50);  // Debouncing delay

    // Increment touch count
    touchCount++;

    // Toggle the LED based on touch count
    if (touchCount == 1 ) {
      digitalWrite(ledPin, HIGH);  // Turn on the LED for the first touch
      Serial.println("Led On");
    } else if (touchCount == 2) {
      digitalWrite(ledPin, LOW);   // Turn off the LED for the second touch
      Serial.println("Led Off");
      touchCount = 0; 
    }

    // Wait for a short duration to avoid multiple touch detections
    delay(500);
  }

  else if ( letter == 'a'){
    touchCount++;

    if (touchCount == 1){
      digitalWrite(ledPin,HIGH);
      Serial.println("Led On");
    }
    else if (touchCount == 2){
      digitalWrite(ledPin,LOW);
      Serial.println("Led Off");
      touchCount = 0;
    }
  }
  
}
