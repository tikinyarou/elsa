def connect():
    import network

    ssid = "AEDC425g"
    password =  "c425c425"

    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("接続済みです")
        return

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print("接続しました")
    print(station.ifconfig())
connect()
