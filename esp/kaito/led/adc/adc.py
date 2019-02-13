from machine import Pin,ADC
from time import sleep_ms
adin = ADC(Pin(35,Pin.IN))
adin.atten(ADC.ATTN_11DB)

while True:
     # val = IDSread()#センサーから読み込む
     val = adin.read()
     # print(pin.value())
     print(val)

     # print(val)#アナログ値を表示する
     # print("  ")
     # print(AnaToCm(val))#距離を表示する
     sleep_ms(300)
