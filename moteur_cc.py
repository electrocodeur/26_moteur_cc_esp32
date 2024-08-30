from machine import Pin, PWM
import time

# Configuration des broches
IN1 = Pin(23, Pin.OUT)
IN2 = Pin(22, Pin.OUT)
ENA = PWM(Pin(21), freq=1000, duty=0)  # Fréquence de 1 kHz

"""
IN3 = Pin(27, Pin.OUT)
IN4 = Pin(26, Pin.OUT)
ENB = PWM(Pin(25), freq=1000, duty=0)  # Fréquence de 1 kHz
"""
# Fonction pour faire tourner le moteur dans un sens
def turn_motor_forward(speed):
    IN1.on()
    IN2.off()
    ENA.duty(speed)

# Fonction pour faire tourner le moteur dans l'autre sens
def turn_motor_backward(speed):
    IN1.off()
    IN2.on()
    ENA.duty(speed)

"""
def turn_motor_right(speed):
    IN3.on()
    IN4.off()
    ENB.duty(speed)

def turn_motor_left(speed):
    IN3.off()
    IN4.on()
    ENB.duty(speed)
"""
# Fonction pour arrêter le moteur
def stop_motor():
    IN1.off()
    IN2.off()
    ENA.duty(0)
    """
    IN3.off()
    IN4.off()
    ENB.duty(0)
    """
# Boucle principale
try:
    while True:
        print("Moteur en avant")
        turn_motor_forward(512)  # 0-1023 (dans ce cas, 512 correspond à 50% de la vitesse)
        time.sleep(5)  # Tourne pendant 5 secondes
        
        print("Moteur en arrière")
        turn_motor_backward(512)  # Tourne dans l'autre sens
        time.sleep(5)  # Tourne pendant 5 secondes
        
        print("Arrêt du moteur")
        stop_motor()
        time.sleep(2)  # Pause de 2 secondes
except KeyboardInterrupt:
    # En cas d'interruption, arrêter le moteur
    stop_motor()
    print("Programme arrêté")
