#include <Arduino.h>

#include <WiFi.h>

#include <ESPmDNS.h> // Dodaj to!


const char* ssid = "KorNet2";
const char* password = "Detergent1$";
WiFiServer server(8888);
WiFiClient client;

#define BRC_PIN 4
#define LED_PIN 2      // Wbudowana dioda LED
#define TIMEOUT_MS 2000 

unsigned long lastWake = 0;
unsigned long lastDataFromROS = 0;
unsigned long lastLedToggle = 0;
bool isRobotRunning = false;
bool failsafeTriggered = false;

void stopRoomba() {
  uint8_t stopCmd[] = {137, 0, 0, 0, 0};
  Serial2.write(stopCmd, 5);
  Serial.println("SAFETY: STOP SENT");
  isRobotRunning = false;
  failsafeTriggered = true;
}

void updateLED() {
  unsigned long now = millis();
  
  // Scenariusz 1: Brak WiFi
  if (WiFi.status() != WL_CONNECTED) {
    if (now - lastLedToggle > 100) { // Szybkie miganie
      digitalWrite(LED_PIN, !digitalRead(LED_PIN));
      lastLedToggle = now;
    }
  } 
  // Scenariusz 2: Failsafe (Utrata połączenia w ruchu)
  else if (failsafeTriggered) {
    if (now - lastLedToggle > 200) { 
       digitalWrite(LED_PIN, !digitalRead(LED_PIN));
       lastLedToggle = now;
    }
  }
  // Scenariusz 3: Połączono z klientem (Praca)
  else if (client && client.connected()) {
    digitalWrite(LED_PIN, HIGH); 
  }
  // Scenariusz 4: Gotowość (WiFi OK, czekamy na ROS2)
  else {
    if (now - lastLedToggle > 1000) { // Wolne miganie
      digitalWrite(LED_PIN, !digitalRead(LED_PIN));
      lastLedToggle = now;
    }
  }
}

void setup() {
  pinMode(BRC_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(BRC_PIN, HIGH);
  
  Serial.begin(115200);
  delay(1000); // Czas na otwarcie monitora szeregowego
  
  Serial.println("\n--- Start Systemu ---");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    Serial.print(".");
  }

  Serial.println("\nWiFi polaczone!");
  Serial.print("IP: "); Serial.println(WiFi.localIP());

  // Konfiguracja mDNS
  if (MDNS.begin("roomba")) {
    Serial.println("mDNS responder uruchomiony: http://roomba.local");
  }

  server.begin();
  server.setNoDelay(true); // Przyspiesza pakiety dla ROS2
  Serial.println("Serwer TCP na porcie 8888 wystartowal!");
  digitalWrite(LED_PIN, HIGH); 
}

void loop() {
  updateLED(); // Aktualizuj stan diody w każdej pętli

  // 1. Keep-alive (BRC)
  if (millis() - lastWake > 60000) {
    digitalWrite(BRC_PIN, LOW);
    delay(500);
    digitalWrite(BRC_PIN, HIGH);
    lastWake = millis();
  }

  // 2. Obsługa WiFi i Klienta
  if (WiFi.status() == WL_CONNECTED) {
    if (!client || !client.connected()) {
      if (isRobotRunning) stopRoomba();
      client = server.available();
      if (client) failsafeTriggered = false; // Reset błędu po nowym połączeniu
    } else {
      // Dane z ROS2 do Roomby
      if (client.available()) {
        lastDataFromROS = millis();
        isRobotRunning = true;
        failsafeTriggered = false;
        while (client.available()) Serial2.write(client.read());
      }

      // Dane z Roomby do ROS2
      while (Serial2.available()) client.write(Serial2.read());

      // 3. Failsafe Check
      if (isRobotRunning && (millis() - lastDataFromROS > TIMEOUT_MS)) {
        stopRoomba();
      }
    }
  }
}