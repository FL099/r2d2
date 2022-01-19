class handleMotor(int):

    status = False
    level = 0.5 # wie stark
    pin = 0 #der GPIO pin auf dem er angeschlossen ist

    def __init__(self, pin):
        self.pin = pin
        return

    def turnOn(self):
        # GPIO auf mit level an Strom aktivieren
        status = True
        print("Motor aktiviert")

    def turnOff(self):
        # GPIO ausschalten
        status = False
        print("Motor gestopt")

    def turnFor(self, ammount):
        # GpIO ammount lange mit level an Strom aktivieren
        status = True;
        print("Motor "+ammount + "sek lang aktiviert")
        status = False;

    def turnForBy(self, ammount, level):
        # GpIO ammount lange mit level an Strom aktivieren
        status = True;
        print("Motor " + ammount + "sek lang aktiviert")
        status = False;