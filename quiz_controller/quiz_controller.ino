#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // initialize the Liquid Crystal Display object with the I2C address 0x27, 16 columns and 2 rows

String python_message = "";
int switchStateTrue = 0; // will attach to PIN2
int switchStateFalse = 0;// will attach to PIN3

void setup() {
  Serial.begin(9600); 

  pinMode(2, INPUT); // TRUE BTN
  pinMode(3, INPUT); // FALSE BTN

  lcd.init();       // initialize the LCD
  lcd.clear();      // clear the LCD display
  lcd.backlight();  // Make sure backlight is on

    // Print a message on both lines of the LCD.
  lcd.setCursor(2, 0);  //Set cursor to character 2 on line 0
  lcd.print("Hey Dylson!");

  lcd.setCursor(2, 1);  //Move cursor to character 2 on line 1
  lcd.print("True or False?");

}

void loop() {
   // RECEIVE: Check if Python sent LED commands
  switchStateTrue = digitalRead(2);
  switchStateFalse = digitalRead(3);
  Serial.print("True");
  // Serial.println(switchStateTrue);
  // Serial.print("Is False?: ");
  // Serial.println(switchStateFalse);

  if (Serial.available() > 0) {
    python_message = Serial.readStringUntil('\n');
    python_message.trim();
    
    lcd.setCursor(0, 0);
    lcd.print(python_message);

    Serial.print("True");
  }

  delay(100);

}
