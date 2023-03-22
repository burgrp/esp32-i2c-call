import mqtt_call
from machine import Pin, I2C

import sys
sys.path.append('/')
import site_config

print('MQTT to I2C bridge')
print('Name:', site_config.name)

act_led = Pin(site_config.act_led, Pin.OUT, value=0)

i2c = I2C(0, scl=Pin(site_config.scl_pin), sda=Pin(site_config.sda_pin), freq=400000)

class Handler:


    # def __init__(self):
    #     self.uart = UART(1, baudrate=2400, tx=21, rx=20, timeout=5000, timeout_char=5000)


    def export_read(self, address):

        act_led.value(1)
        try:
            data = i2c.readfrom(address, 1)
            return data[0]
        finally:
            act_led.value(0)

    def export_write(self, address, value):
        act_led.value(1)
        try:
            i2c.writeto(address, bytes(value))
        finally:
            act_led.value(0)

    def export_scan(self):
        return i2c.scan()

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
