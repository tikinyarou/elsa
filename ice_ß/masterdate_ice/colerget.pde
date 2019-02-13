void getcoler() {

  frameRate(fps);      // フレームレートの設定

  fill(0);
  rect(0, h_img, w_img, h_img*2);

  if (cam.available()) {
    cam.read();       // カメラ画像を読み込んで
    set(0, 0, cam); // 画面に表示　


    //difRed < tolerance && difGreen < tolerance && difBlue < tolerance && 

    detection=false;//物体検知のフラグをfalse（検知なし）にしておく
    if (key == 'a') {
      for (int i=0; i< w_img*h_img; i++)  //画面全体のピクセル数だけ繰り返し処理
      {
        //物体の色と各ピクセルの色の差を求める（RGB３色分）
        float difRed=abs(red(targetColor)-red(cam.pixels[i]));
        float difGreen=abs(green(targetColor)-green(cam.pixels[i]));
        float difBlue=abs(blue(targetColor)-blue(cam.pixels[i]));


        //if (key == 't') {
        if (difRed < tolerance && difGreen < tolerance && difBlue < tolerance) {
          //左端、右端のX座標、上端、下端のY座標を導く
          //difRed < tolerance && difGreen < tolerance && difBlue < toleranc

          detection=true;
          xmin=min(i%w_img, xmin);//左端（X最小値）
          xmax=max(i%w_img, xmax);//右端（X最大値）
          ymin=min(i/w_img, ymin);//上端（Y最小値）
          ymax=max(i/w_img, ymax);//下端（Y最大値）

          set(i%w_img, i/w_img+h_img, targetColor);
        }
      }
      //}

      if (detection==true) {//物体検知有りの場合

        x1=xmin;
        x2=xmax;
        y1=ymin;
        y2=ymax;

        //左端、右端、上端、下端の座標値を初期化しておく
        xmin=w_img;
        xmax=0;
        ymin=h_img;
        ymax=0;
      }

      x3=x1-a;
      y3=y1+h_img-a;
      x4=x2-x1+a*2;
      y4=y2-y1+a*2;


      //myPort.write(getcoler);


      noFill();
      stroke(255, 0, 0);
      rect(x3, y3, x4, y4);

      String s;//物体検知有無表示の文字列変数
      if (detection==true) {//物体検知有りの場合
        s="detected";//表示：「検知」
      } else {
        s="none";//表示：「なし」
      }

      //以下は各値の表示
      fill(targetColor);//指定した物体の色
      rect(0, h_img, b, b);//矩形表示
      text(tolerance+": "+s, 20, h_img+b);//文字列表示（許容値：物体検知有無）
      text(x1+":"+y1+":"+x2+":"+y2, 10, h_img+b*2);
      text(x3+":"+y3+":"+x4+":"+y4, 10, h_img+b*3);
    }

    if (key == 's') {
      for (int i=0; i< w_img*h_img; i++)  //画面全体のピクセル数だけ繰り返し処理
      {

        //物体の色と各ピクセルの色の差を求める（RGB３色分）
        float difRed=abs(red(targetColor)-red(cam.pixels[i]));
        float difGreen=abs(green(targetColor)-green(cam.pixels[i]));
        float difBlue=abs(blue(targetColor)-blue(cam.pixels[i]));

        color currColor = cam.pixels[i];
        color bkgdColor = backgroundPixels[i];

        int currR = (currColor >> 16) & 0xFF;
        int currG = (currColor >> 8) & 0xFF;
        int currB = currColor & 0xFF;

        int bkgdR = (bkgdColor >> 16) & 0xFF;
        int bkgdG = (bkgdColor >> 8) & 0xFF;
        int bkgdB = bkgdColor & 0xFF;

        int diffR = abs(currR - bkgdR);
        int diffG = abs(currG - bkgdG);
        int diffB = abs(currB - bkgdB);

        //if (key == 'r') {
        if (diffR + diffG + diffB > noiseFilter) {
          if (difRed < tolerance && difGreen < tolerance && difBlue < tolerance) {
            pixels[i] = color(targetColor);
            detection=true;
            x2min=min(i%w_img, x2min);//左端（X最小値）
            x2max=max(i%w_img, x2max);//右端（X最大値）
            y2min=min(i/w_img, y2min);//上端（Y最小値）
            y2max=max(i/w_img, y2max);//下端（Y最大値）

            set(i%w_img, i/w_img+h_img, targetColor);
          }
        }
      }
      //}

      if (detection==true) {//物体検知有りの場合

        x6=x2min;
        x7=x2max;
        y6=y2min;
        y7=y2max;

        //左端、右端、上端、下端の座標値を初期化しておく
        x2min=w_img;
        x2max=0;
        y2min=h_img;
        y2max=0;
      }

      x8=x6-a;
      y8=y6+h_img-a;
      x9=x7-x6+a*2;
      y9=y7-y6+a*2;

      noFill();
      stroke(255);
      rect(x8, y8, x9, y9);

      String s;//物体検知有無表示の文字列変数
      if (detection==true) {//物体検知有りの場合
        s="detected";//表示：「検知」
      } else {
        s="none";//表示：「なし」
      }

      //以下は各値の表示
      fill(targetColor);//指定した物体の色
      rect(0, h_img, b, b);//矩形表示
      text(tolerance+": "+s, 20, h_img+b);//文字列表示（許容値：物体検知有無）
      text(x6+":"+y6+":"+x7+":"+y7, 10, h_img+b*2);
      text(x8+":"+y8+":"+x9+":"+y9, 10, h_img+b*3);
    }
    getercoler = y4;
    //println(y4);
    getercoler2 = y9;
    //println(y9);rtt

    if (key == 'v') {
      getercoler = 0;
      //println(y4);
      getercoler2 = 0;
    }

    if (getercoler > getercoler2 && flag == 1) {
      servo = 120;
      myPort.write(servo);
    } //else 
    if (getercoler <= getercoler2) {
      flag = 0;
      servo = 50;
      myPort.write(servo);
    }
    //} else if (flag == 0) {
    //  servo = 0;
    //  myPort.write(servo);
    //} else {
    //  servo = 0;
    //  myPort.write(servo);
    //}
  }
  //println(servo);
  //println(y4);
  //println(y9);
  println(flag);
}

void serialEvent(Serial p) {
  flag = myPort.read();
  //println(flag);
}