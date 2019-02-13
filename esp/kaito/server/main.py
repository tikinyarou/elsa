import socket
import machine


# ブラウザに表示させるためのhtml
# ポートは自身の環境に合わせてください
html = """
<!DOCTYPE html>
<html>
<head>
  <title>Canvas test</title>
</head>
<!-- <canvas id="canvas" width="800px" height="600px" style="border:1px solid #000;background-color: #fffac;" ></canvas> -->

<body style='margin: 0'>
  <canvas id="canvas">
    sorry,your browser is rubbish.
  </canvas>
  <script src="main.js"></script>
</body>
</html>
"""

LED_4 = machine.Pin(4, machine.Pin.OUT)

#サーバー関係と制御n
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.11.5', 80))
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
