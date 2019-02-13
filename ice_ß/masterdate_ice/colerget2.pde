void get2() {
  
  frameRate(fps);      // フレームレートの設定
  fill(0);
  rect(0, h_img, w_img, h_img*2);
  if (cam.available()) {
    cam.read();       // カメラ画像を読み込んで
    set(0, 0, cam); // 画面に表示　

    detection=false;//物体検知のフラグをfalse（検知なし）にしておく

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