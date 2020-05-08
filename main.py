import time
import serial
# Importa o publish do paho-mqtt
import paho.mqtt.publish as publish

ser = serial.Serial('/dev/ttyACM0', 9600)

contador = 0

# Broker do Thingspeak
host_name = "mqtt.thingspeak.com";

# Channel ID do Thingspeak
user = "1040541";

# Write API Key do Thingspeak
pwd = "CAXEC5ZB8C3C2BQ2";

# Numero do campo (field) que deseja enviar o valor
nro_campo = "1";

topic = "channels/"+user+"/publish/fields/field"+nro_campo+"/"+ pwd;

time.sleep(1.5)

while (contador < 300):
	contador = contador + 1
	# Valor a enviar
	valor = ser.readline()

	# Publica ao canal
	publish.single(topic, valor, hostname=host_name);


