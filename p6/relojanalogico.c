// This #include statement was automatically added by the Particle IDE.
#include <neopixel.h>



#define PIXEL_COUNT 24
#define PIXEL_PIN D6
#define PIXEL_TYPE WS2812B
#define YELLOWDARK 40, 25, 10
#define PEACH 120,40,5
#define CYAN 10,150,70
#define PURPLE 30,3,30
#define BLUE 5,5,30
#define WHITE 150,150,150
#define GREEN 10,180,10
#define RED 30,0,0
#define YELLOW 227,201,17
#define APAGADO 0,0,0
Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN, PIXEL_TYPE);
int timezone = -6; //change time zone
int i;
int j;
int m;
void setup() {
 Serial.begin(57600);
 pinMode(7,OUTPUT);
 digitalWrite(7,0);
 strip.begin();
}

void loop() {
    getTime();
    //Serial.print(Time.hour());
    //Serial.print(" : ");
    //Serial.print(Time.minute());
    //Serial.print(" : ");
    //Serial.println(Time.second());
    //delay(1000);
    //spinrapido(YELLOWDARK);
    //spinseg(BLUE);
    //delay(1900);
    //spinrapido(APAGADO);
    //delay(150);
    spinmin(RED);
    delay(2200);
    spinrapido(APAGADO);
    delay(200);
    spin(PURPLE);
    delay(3700);
    spinrapido(APAGADO);
    delay(200);

    

}

void spinrapido(int R, int G, int B){
    for(i=0; i < PIXEL_COUNT; i++) {
        strip.setPixelColor(i, R, G, B);
        strip.show();
        delay(40);
        
       
    }
}

void spin(int R, int G, int B) {
    for(j=0; j < Time.hour()*2; j = j + 2) {
        strip.setPixelColor(j, R,G,B);
        strip.show();
        delay(190);
    }
    
}

void spinmin(int Q, int W, int E) {
    for(i=0; i < Time.minute()/2.5; i = i + 2) {
        strip.setPixelColor(i, Q,W,E);
        strip.show();
       delay(120);
    }
    
}

void spinseg(int A, int S, int D) {
    int var_sec;
    for(i=0; i < Time.second()/2.5; i++) {
        strip.setPixelColor(i, A,S,D);
        strip.show();
        delay(60);
    }
    
}

int getTime(){
    Time.zone(timezone);
    return (Time.hour())+Time.minute()+Time.second(); //24 hour
    //return (Time.hourFormat12())*100+Time.minute(); //12 hour
}