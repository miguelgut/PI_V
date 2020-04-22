# Importa o publish do paho-mqtt
import paho.mqtt.publish as publish

# Broker do Thingspeak
host_name = "mqtt.thingspeak.com";

# Channel ID do Thingspeak
user = "1040541";

# Write API Key do Thingspeak
pwd = "CAXEC5ZB8C3C2BQ2";

# Numero do campo (field) que deseja enviar o valor
nro_campo = "1";

topic = "channels/"+user+"/publish/fields/field"+nro_campo+"/"+ pwd;

# Valor a enviar
valor = 5;

# Publica ao canal
publish.single(topic, valor, hostname=host_name);
