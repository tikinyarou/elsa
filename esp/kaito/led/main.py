from machine import Pin
import socket
from neopixel import NeoPixel
import time

html = """
<!DOCTYPE html>
<html>
<head>
  <title>test led</title>

  <style type="text/css">
    body{
      font-family: "Helvetica Neue",Helvetica;
    }
    .picker{
      position: absolute;
      top: auto;
      bottom: 0;
      left: 0;
      right: 0;
      margin: auto;
      width: 780px;
      height: 180px;
    }
    #display{
      width: 100%;
      height: 100px;
      background: #730aa2;
      transition: background 100ms;
      margin-top: 30px;
      border: 1px solid #000;
    }
    input{
      display: block;
      width: 100%;
    }
  </style>
</head>
<body>
  <div class="picker">
    RED  <input type="range" min="0" max="255" step="1" id="red" value="167">
    GREEN<input type="range" min="0" max="255" step="1" id="green" value="32">
    BLUE <input type="range" min="0" max="255" step="1" id="blue" value="54">
    <div id="display"></div>
  </div>
  <script type="text/javascript">
    var input = document.querySelectorAll("input");

    for(var i = 0; i < input.length; i++){
      input[i].addEventListener("input",function(){
        var red = document.getElementById("red").value,
            green = document.getElementById("green").value,
            blue = document.getElementById("blue").value;

        var display = document.getElementById("display");
        display.style.background = "rgb(" + red +","+ green +","+ blue +")";
      });
    }
  </script>
</body>
</html>

"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.80', 80))
s.listen(5)



while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)
    LEDON_4 = request.find('/?LED=ON_4')
    LEDOFF_4 = request.find('/?LED=OFF_4')

    if LEDON_4 == 6:
        LED_4.value(1)
    if LEDOFF_4 == 6:
        LED_4.value(0)
    response = html
    conn.send(response)
    conn.close()

# def demo(pin, n):
#     np = NeoPixel(Pin(pin), n)
# # //post
# # //ayaxs
# # //websocet
#     # cycle
#     for i in range(4 * n):
#         for j in range(n):
#             np[j] = (0, 0, 0)
#         np[i % n] = (25, 5, 55)
#         np.write()
#         time.sleep_ms(25)
#
#     # bounce
#     for i in range(4 * n):
#         for j in range(n):
#             np[j] = (0, 0, 128)
#         if (i // n) % 2 == 0:
#             np[i % n] = (0, 0, 0)
#         else:
#             np[n - 1 - (i % n)] = (0, 0, 0)
#         np.write()
#         time.sleep_ms(60)
#
#     # fade in/out
#     for i in range(0, 4 * 256, 8):
#         for j in range(n):
#             if (i // 256) % 2 == 0:
#                 val = i & 0xff
#             else:
#                 val = 255 - (i & 0xff)
#             np[j] = (val, 0, 0)
#         np.write()
#
#     # clear
#     for i in range(n):
#         np[i] = (0, 0, 0)
#     np.write()
#
# demo(4,90)
