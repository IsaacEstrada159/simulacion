// This #include statement was automatically added by the Particle IDE.
#include <Adafruit_SI1145.h>

// Connect Vin to 3-5VDC
// Connect GND to ground
// Connect SCL to I2C clock pin (D1 on Photon/Electron)
// Connect SDA to I2C data pin  (D0 on Photon/Electron)


#include "Adafruit_Si7021.h"   // Use for Build IDE


Adafruit_SI1145 uv = Adafruit_SI1145();
Adafruit_Si7021 sensor = Adafruit_Si7021();

void setup() {
  Serial.begin(115200);
  Serial.println("Si7021 test");
  sensor.begin();
}

void loop() {

  Serial.println("===================");
  Particle.publish("Vis: ", String(uv.readVisible()));
  Particle.publish("IR: ", String(uv.readIR()));
  
  // Uncomment if you have an IR LED attached to LED pin!
  //Serial.print("Prox: "); Serial.println(uv.readProx());

  float UVindex = uv.readUV();
  // the index is multiplied by 100 so to get the
  // integer index, divide by 100!
  UVindex /= 100.0;  
  Particle.publish("UV: ",  String(UVindex));


  Particle.publish("nivel de luz", String(analogRead(A4)));
  Particle.publish("nivel de pila", String(analogRead(A5)));
  Particle.publish("humedad", String(sensor.readHumidity(), 2));
  Particle.publish("temperatura", String(sensor.readTemperature() - 3.85, 2));
  
    
  Serial.print("nivel de luz"); Serial.print(analogRead(A4));
  Serial.print("  nivel de pila"); Serial.print(analogRead(A5));
  Serial.print(" Humidity:    "); Serial.print(sensor.readHumidity(), 2);
  Serial.print("\tTemperature: "); Serial.println(sensor.readTemperature() - 3.35, 2);
  delay(100000);
}