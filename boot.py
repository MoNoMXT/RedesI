import network

def create_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='MyESP32AP', authmode=network.AUTH_WEP, password='12345')
    print('AP created, IP:', ap.ifconfig()[0])

create_ap()
