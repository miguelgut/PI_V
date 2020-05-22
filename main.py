import time
import serial
# Importa o publish do paho-mqtt
import paho.mqtt.publish as publish
import usb.core
import usb.util
import peripheral

# Broker do Thingspeak
host_name = "mqtt.thingspeak.com"

# Channel ID do Thingspeak
user = "1040541"

# Write API Key do Thingspeak
pwd = "CAXEC5ZB8C3C2BQ2"

# Numero do campo (field) que deseja enviar o valor
nro_campo = "1"

topic = "channels/"+user+"/publish/fields/field"+nro_campo+"/"+ pwd;

print(peripheral.EnumerateUSB())
contador = 0
while (contador < 60):
	contador = contador + 1
	# Valor a enviar
	valor = peripheral.DevicesAttached()

	# Publica ao canal
	print("Enviando valor: " + str(valor))
	print("contador: " + str(contador))
	publish.single(topic, valor, hostname=host_name)
	time.sleep(5)

