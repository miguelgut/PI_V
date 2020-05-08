#define tempoContador 10000
#define inputTensao 0
#define ledSaida 7
#define valorAcionamento 6
#include <Arduino.h>
#include <timer.h>

auto timer = timer_create_default();
double valorTensao;
int countAcionamentos = 0;

void setup() { 
  pinMode(ledSaida, OUTPUT);
  timer.every(tempoContador, controleAcionamento);
  timer.every(500, controleSensor);
  timer.every(9500, controleLed);
  Serial.begin(9600); 
}

bool controleLed(void *){
   Serial.println("Vou apagar");
  digitalWrite(ledSaida, LOW);  
  return true;
}

bool controleSensor(void *){
  valorTensao = 10*(analogRead(inputTensao))/1023;
  Serial.println(valorTensao);
  if(valorTensao >= valorAcionamento){
    countAcionamentos++;
  }
  return true;  
}

bool controleAcionamento(void *) {
    
    Serial.println("Contagem de acionamentos:");
    Serial.println(countAcionamentos);
    if(countAcionamentos >= 3){
      digitalWrite(ledSaida, HIGH);  
    }else{
      digitalWrite(ledSaida, LOW);  
    }

    countAcionamentos = 0;
    return true;
}

void loop() {
  timer.tick();
}
