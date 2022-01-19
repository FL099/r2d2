class handleLed(int):

    status = False
    pin = 0 #der GPIO pin auf dem es angeschlossen ist

    def __init__(self, pin):
        self.pin = pin
        return

    def turnOn(self):
        #GPIO auf on setzen
        status = True
        print("Led aktiviert")

    def turnOff(self):
        # GPIO auf off setzen
        status = False
        print("Led deaktiviert")