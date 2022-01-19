from parts import Led
from parts import Motor
import threading

print("Hi, ich bin R2D2")

print("---------")
print("Anfangs werde ich hier alle mit-loggen:")

try:
    f = open("logfile.txt", "a")
    f.write("Log----------\n")
except:
    print("no logging available, something went wrong")



# Fortbewegung
r_mot = Motor.handleMotor(2) # rechter Motor (bein)
l_mot = Motor.handleMotor(3) # linker Motor (bein)
head_mot = Motor.handleMotor(4) # kopf drehen

# Fortbewegung optional
l_leg_mot = Motor.handleMotor(5) # fahr/standmodus wechseln 1/2
r_leg_mot = Motor.handleMotor(6) # fahr/standmodus wechseln 2/2

def takeAction(inputVal):
    inputVal = inputVal.upper()
    if inputVal == 'W':
        f.write("Vorwärts")
        return "Vorwärts"
    elif inputVal == 'S':
        f.write("Rückwärts")
        return "Rückwärts"

    f.write("Ungültige Eingabe")
    return "Ungültige Eingabe"



#Hier werden die ganzen Komponenten Pins zugeordnet
onOffLed = Led.handleLed(1) # zeigt, ob er an ist
volume = 5 # Output Lautstärke
head_rotation = 0 # 0= vorne 360 = hinten



# testzwecke
i = 0
while 1 < 2:
    if i >= 5:
        break

    takeAction(input("Was soll ich tun?"))
    i += 1
    f.write("-loop " + str(i) +"\n")




f.close()

# Sensoren
#ir_in # IR Receiver
#collision # Ultraschallsensor
#wet # Feuchtigkeitssensor
#temperature #Thermometer
#air_qual # Gassensor




# test ob Led an/aus funktioniert
onOffLed = Led.handleLed(1)
onOffLed.turnOn()

