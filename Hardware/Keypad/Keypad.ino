/* @file HelloKeypad.pde
|| @version 1.0
|| @author Alexander Brevig
|| @contact alexanderbrevig@gmail.com
||
|| @description
|| | Demonstrates the simplest use of the matrix Keypad library.
|| #
*/
#include <Keypad.h>

#define LED_green_pin 9
#define LED_red_pin 11

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[ROWS] = {5, 4, 3, 2}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {8, 7, 6}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup(){
  Serial.begin(9600);
  pinMode(LED_green_pin, OUTPUT);
  pinMode(LED_red_pin, OUTPUT);
  digitalWrite(LED_green_pin, HIGH);
  digitalWrite(LED_red_pin, LOW);
}
  
void loop(){

  if (Serial.available() > 0) {
    String msg = Serial.readString();

      if (msg == "ON") {
        digitalWrite(LED_green_pin, HIGH);
        digitalWrite(LED_red_pin, LOW);
      }
      else if (msg == "OFF") {
        digitalWrite(LED_green_pin, LOW);
        digitalWrite(LED_red_pin, HIGH);  
      }
    
  }

  char key = keypad.getKey();
  
  if (key){
    Serial.println(key);
  }
}
