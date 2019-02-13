esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART write_flash -z 0x1000 /Users/aed/Downloads/esp32-20180201-v1.9.3-250-ga44892dd.bin

screen /dev/cu.SLAB_USBtoUART 115200

ampy -p /dev/cu.SLAB_USBtoUART ls
ampy -p /dev/cu.SLAB_USBtoUART put main.py

esptool.py --port /dev/cu.SLAB_USBtoUART erase_flash

#上がesp32の色々
#下がesp02

esptool.py --port=/dev/cu.usbserial-DN02BCFD --baud 115200 chip_id
#接続されているか確かめる
esptool.py --port=/dev/cu.usbserial-DN02BCFD --baud 115200 flash_id
#フラッシュメモリのサイズ確認
sudo esptool.py --port /dev/cu.usbserial-DN02BCFD erase_flash
#全消し
esptool.py --port=/dev/cu.usbserial-DN02BCFD --baud 115200 write_flash --flash_size=32m 0 ./esp8266-20171101-v1.9.3.bin
#ファーム書き込み
sudo cu -s 115200 -l /dev/cu.usbserial-DN02BCFD
sudo screen /dev/cu.usbserial-DN02BCFD 115200
#ターミナルから直に命令
ampy -p /dev/cu.usbserial-DN02BCFD put
ampy -p /dev/cu.usbserial-DN02BCFD ls
