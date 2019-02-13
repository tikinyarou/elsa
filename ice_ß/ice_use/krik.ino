int wclick() {

   click_flag_1 = digitalRead(switch_pin);

  //一回目のクリックがされた場合
  if(click_flag_1 == 0){

    //0.2秒内にスイッチが離された場合、click_flag_1==1の状態でループから出る
    for(int i=0; i<10; i++){
      click_flag_1 = digitalRead(switch_pin);
      if(click_flag_1 == 1)break;
      delay(20);
    }

    //もしスイッチが離されたならダブルクリックか
    //シングルクリックなのかを確認するループに入る
    if(click_flag_1 == 1){

      //0.2秒内にスイッチが押された場合、clck_flag_2==0の状態でループから出る
      for(int i=0; i<10; i++){
        click_flag_2 = digitalRead(switch_pin);
        if(click_flag_2==0)break;
        delay(20); //20ms
      }

      //click_flag==0であればそれをダブルクリックとする
      if(click_flag_2 == 0){
        flag = 0;
        click_flag_2 = 1;
        delay(50);

        //もしclick_flag==0でない場合はシングルクリックとする
      }
      else{
        flag = 1;
      }
    }
    Serial.write(flag);
    //Serial.println(flag);
  }
  delay(100); //ここの数値を小さくすると上手く動かなくなるので注
}
