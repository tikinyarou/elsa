#include <Servo.h>

Servo myservo;

//int servo = 10;
int switch_pin = 6;
int a = 0 ;
int i ;
int count = 0;
int flag = 0;
int click_flag_1 = 1 , click_flag_2 = 1;

void setup() {
  Serial.begin(9600);
  pinMode(switch_pin, INPUT);
  pinMode(12,OUTPUT);
  myservo.attach(9);
}

void loop() {
  wclick();
  if(Serial.available()>0){
    
    int servo = Serial.read();
    //int x=map(val,0,255,0, 179);
    myservo.write(servo);
  }
  delay(15);
 // delay(15);
//  servo = Serial.read();
//  no = Serial.read();
//  if(no == 1){
//  myservo.write(servo);
//  }
//  Serial.write(flag);
}
