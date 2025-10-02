// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250623
// VERSION: 1.0
// FILE: mydigifarm,1.0,demoOnly-liteCluster.cpp
// DESCRIPTION: General readme file.  
// LASTMODIFIED: 20250721

//! .cpp

// Introduction

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables, calibrate the sensors for expected defaults, and configure libraries to use particular sensor configurations based on type and library requirements. 
// *|*|*|*|* Section 1 *|*|*|*|*

// This section imports the necessary libraries to talk to the arduino as well as the sensors.  
#include <DHT.h>
#include <DHT_U.h>
#include <Arduino.h>
#include <EEPROM.h>

// This sets the type of dht sensor we are working with and should be modified if you are using another sensor type. 
#define DHTTYPE DHT11

// These are variable that set up the expected pin values between the arduino and sensors. 
int const printPin = 12;
int const dhtPin = 2;
int const ldrPin = A0;
int const soilPin = A1;

// Sets the default values we are expecting for the soil moisture sensor. Your sensor can be calibrated modifying these numbers. 
int const wetSensor = 239;
int const drySensor = 595;

// These are additional variables populated by the sensors output data and used by the system to generate the data pill. 
float t = 0;
float h = 0;
int ldrVal = 0;
int soilVal = 0;
String data_pill;

// Configuring dht from the DHT library. This sets the pin being used and sensor type.
DHT dht( dhtPin, DHTTYPE );

// *|*|*|*|* End Section 1 *|*|*|*|*

// *|*|*|*|* Start Section 2 *|*|*|*|*
// Section 2 covers setting up classes and functions. 
// This is where the initial device setup and subsequent functions are created that do all of the work gathering data and formatting it. 
// Most functions are created here and used in the next section. 
// *|*|*|*|* Section 2 *|*|*|*|*

// Writes a Demo ID to the eeprom of the device for identification, starts the serial connection, and starts printing temperature and humidity data from the sensor. 
void setup(){
  int b1=155;  
  int b2=222; 
  int b3=24;  
  int b4=47;  
  int b5=80;  
  int b6=196; 
  int b7=94;  
  int b8=29;  
  int b9=128;
  EEPROM.write(0,b1);
  EEPROM.write(1,b2);
  EEPROM.write(2,b3);
  EEPROM.write(3,b4);
  EEPROM.write(4,b5);
  EEPROM.write(5,b6);
  EEPROM.write(6,b7);
  EEPROM.write(7,b8);
  EEPROM.write(8,b9);
  Serial.begin( 9600 );
  pinMode( printPin, INPUT);
  dht.begin();
}

// Formats the data from the dht to match the data pill. 
void get_dht(float* t, float* h) {
  *t = dht.readTemperature();
  *h = dht.readHumidity();
}

// Gathers the photosensor data and formats it to the data pill. 
void get_ldr(int* ldrVal){
  *ldrVal = analogRead(ldrPin);
}

// Gathers the soil moisture data and formats it to the data pill.
void get_soil(int* soilVal){
  int sensorVal = analogRead(soilPin);
  *soilVal = map(sensorVal, wetSensor, drySensor, 100, 0);
}

// Outputs the collected arduino sensor data from the data pill. 
void print_pill(float * temp, float * humi, int * ldrRead, int * soilRead){
  int readbyte=0;
  for (int i = 0; i <= 8; i++) { 
  readbyte = EEPROM.read(i);
  char arduinoID = "";
    if (readbyte < 0x10)
      arduinoID = arduinoID + Serial.print("0");
    arduinoID = arduinoID + Serial.print(readbyte, HEX);
  }
  Serial.print(F("|"));
  Serial.print( *temp );
  Serial.print(F("|"));
  Serial.print( *humi );
  Serial.print(F("|"));
  Serial.print(*ldrRead);
  Serial.print(F("|"));
  Serial.print(*soilRead);
  Serial.println();
}

// Gathers the data from the functions and creates the data pill. 
void build_pill(){
  float temp, humi;
  int ldrRead;
  int soilRead;
  get_dht(&temp, &humi);
  get_ldr(&ldrRead);
  get_soil(&soilRead);
  print_pill(&temp, &humi, &ldrRead, &soilRead);
}

// *|*|*|*|* End Section 2 *|*|*|*|*

// *|*|*|*|* Start Section 3 *|*|*|*|*
// Section 3 is the loop of code that runs repeatedly. The code below typically calls the functions created in section 2 in a logical order. 
// We use this to gather the data from the Arduino and present it to the Raspberry Pi. 
// Another job on the Rasperry Pi takes this data as presented and writes it to the database.
// *|*|*|*|* Section 3 *|*|*|*|*

// Runs the program. Waits for a second between attempts, then tries to read the sensors and generate the datapill. 
// If serial connections exist attempts to read and add data to data pill. 
void loop(){
  delay(1000);
  int printPinState = digitalRead(printPin);
  if(printPinState == 0){
    build_pill ();
  }
  if( Serial.available() > 0 ){
    char serialIn = 0;
    serialIn = Serial.read();
    if( serialIn == '1' ){
      build_pill ();
    }
  }
}

// *|*|*|*|* End Section 3 *|*|*|*|*

// -10920
// Copyright 2025 mydigifarm
