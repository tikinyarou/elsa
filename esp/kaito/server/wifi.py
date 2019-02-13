def do_connect(ssid,pw):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('setuzoku ok nakanji yade-')
        sta_if.active(True)
        sta_if.connect(ssid,pw)

        while not sta_if.isconnected():
            pass

    print('network config:',sta_if.ifconfig())

do_connect('mstid','mediascience')
