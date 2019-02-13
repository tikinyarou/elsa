//test034
import processing.video.*;
import gab.opencv.*;
import controlP5.*;
import processing.serial.*;

Serial myPort;

OpenCV opencv;
Capture cam;

ControlP5 cp5;
int myColor = color(0, 0, 0);
int Tolerance = 100;
int t = 0;
int r = 0;
int keisoku;
int hikaku;

int w_img = 640;       
int h_img = 480;           
int p_text_size = 30;      
int fps = 15;

int tolerance=15;//色許容値用の変数（後で調整可）
color targetColor=color(255, 255, 255);//物体の色用の変数（後で変更可)

color white = color(255, 255, 255);

int x, y, x1, y1, x2, y2, x3, y3, x4, y4;//図形座標用変数
int xmin=w_img, xmax=0;//左端X座標、右端X座標
int ymin=h_img, ymax=0;//上端Y座標、下端Y座標 

int x5, y5, x6, y6, x7, y7, x8, y8, x9, y9;//図形座標用変数
int x2min=w_img, x2max=0;//左端X座標、右端X座標
int y2min=h_img, y2max=0;//上端Y座標、下端Y座標 

int a=5;//余白
int b=15;//行間

boolean detection=false;//物体検知のフラグ 

int numPixels;    //画像のピクセルの総数
int[] backgroundPixels;    //背景のピクセル
int noiseFilter = 50;    //ノイズを拾わないためのフィルタ（値を増やすとフィルタが強くかかる）

int flag = 0;
int on = 0;
int servo = 0;
int getercoler;
int getercoler2;

void setup() {
  size(640, 960);  // 画面サイズの設定

  myPort=new Serial(this, Serial.list()[1], 9600);
  myPort.write(0);

  String[] cameras = Capture.list();
  if (cameras.length == 0) {
    println("There are no cameras available for capture.");
    exit();
  } else {
    println("Available cameras:");
    for (int i = 0; i < cameras.length; i++) {
      println(cameras[i]);      // カメラの名
    }

    cam = new Capture(this, 640, 480, "UCAM-DLN130T series");
    cam.start();

    opencv = new OpenCV(this, 640, 480);

    opencv.startBackgroundSubtraction(5, 3, 0.5);

    loadPixels();

    numPixels = cam.width * cam.height;
    //現在のキャプチャ画像と比べるために背景画像用の配列を作る
    backgroundPixels = new int[numPixels];
  }

  //キャプチャーするビデオ画像の総ピクセル数
  numPixels = cam.width * cam.height;
  //現在のキャプチャ画像と比べるために背景画像用の配列を作る
  backgroundPixels = new int[numPixels];
  loadPixels();

  noStroke();
  cp5 = new ControlP5(this);
  cp5.addSlider("Tolerance")
    .setPosition(10, 300)
    .setSize(20, 150)
    .setRange(0, 100)
    ;

  cp5 = new ControlP5(this);
  cp5.addButton("keisoku")
    .setLabel("keisoku")
    .setPosition(50, 300)
    .setSize(80, 40)
    .setColorCaptionLabel(t = 1);
  ;
  
}

void draw() {

  getcoler();

  tolerance = Tolerance;
}

/*
void Flag(){
 
 if (detection==false && getercoler > getercoler2) {
 on = 1;
 } if (on == 1 && flag == 1) {
 servo = 100;
 myPort.write(servo);
 } else if (detection == true && getercoler == getercoler2) {
 servo = 0;
 myPort.write(servo);
 }
 println(servo);
 }
 
 void serialEvent(Serial p) {
 flag = myPort.read();
 //println(flag);
 }
 */

void mousePressed() {//クリックしたら
  //マウス座標上のピクセルの色（物体の色）を記憶しておく
  targetColor=cam.pixels[mouseX+mouseY*w_img];
  cam.loadPixels();
  arraycopy(cam.pixels, backgroundPixels);
}

void keyPressed() {

  if (key == ' ') {
    exit();
  }

  if (key==CODED) {
    if (keyCode==LEFT) {//左キーを押した場合
      tolerance-=1;   //許容値を-1する
    }
    if (keyCode==RIGHT) {//右キーを押した場合
      tolerance+=1;    //許容値を+1する
    }
  }
}