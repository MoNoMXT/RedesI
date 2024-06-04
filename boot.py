import network
import time

def create_ap_wep():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    try:
        ap.config(essid='MyESP32AP', authmode=network.AUTH_WEP, password='12345')
    except Exception as e:
        print("Error al configurar el AP:", e)
    
    # Esperar a que el punto de acceso esté activo
    timeout = 10
    while not ap.active() and timeout > 0:
        print('Esperando a que el AP esté activo...')
        time.sleep(1)
        timeout -= 1

    if ap.active():
        print('AP creado, IP:', ap.ifconfig()[0])
    else:
        print('Error al crear el AP')

create_ap_wep()