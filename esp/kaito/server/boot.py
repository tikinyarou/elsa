# SSID_NAME = "AEDC425g"
# SSID_PASS = "c425c425"

SSID_NAME = "mstid"
SSID_PASS = "mediascience"

import utime
import network
# ==== connecti to wifi access point ============================================
def connect_wifi(ssid, passkey, timeout=10):
    wifi= network.WLAN(network.STA_IF)
    if wifi.isconnected() :
        print('already Connected.    connect skip')
        return wifi
    else :
        wifi.active(True)
        wifi.connect(ssid, passkey)
        while not wifi.isconnected() and timeout > 0:
            print('.')
            utime.sleep(1)
            timeout -= 1

    if wifi.isconnected():
        print('ok')
        return wifi
    else:
        print('no')
        return null

wifi = connect_wifi(SSID_NAME, SSID_PASS)
if not wifi :
    sys.exit(0)
