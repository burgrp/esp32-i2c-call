import mqtt_call

import sys
sys.path.append('/')
import site_config


print('MQTT to I2C bridge')
print('Name:', site_config.name)

class Handler:


    # def __init__(self):
    #     self.uart = UART(1, baudrate=2400, tx=21, rx=20, timeout=5000, timeout_char=5000)


    def export_read(self, address):
        return address + 100

    def export_write(self, address, value):
        return address + value


    def export_get_status(self):
        return {
            "rssi": server.mqtt_client._sta_if.status('rssi'),
            "ip": server.mqtt_client._sta_if.ifconfig()[0]
        }


server = mqtt_call.Server(
    handler=Handler(),
    name=site_config.name,
    wifi_ssid=site_config.wifi_ssid,
    wifi_password=site_config.wifi_password,
    mqtt_broker=site_config.mqtt_broker,
    ledPin=site_config.wifi_led,
    debug=site_config.debug
)

server.dump()
server.start()
