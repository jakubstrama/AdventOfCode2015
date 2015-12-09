class Light:
    state = None

    def __init__(self, state):
        self.state = state

    def turnOff(self):
        self.state = False

    def turnOn(self):
        self.state = True

    def toggle(self):
        self.state = not self.state

    def runCommand(self, command):
        if(command.startswith("turn on")):
            self.turnOn()
        if(command.startswith("turn off")):
            self.turnOff()
        if(command.startswith("toggle")):
            self.toggle()


class Light2:
    lightness = 0

    def __init__(self, state):
        self.lightness = state

    def turnOn(self):
        self.lightness += 1

    def turnOff(self):
        if(self.lightness > 0):
            self.lightness -= 1
        else:
            self.lightness = 0

    def toggle(self):
        self.lightness += 2

    def runCommand(self, command):
        if(command.startswith("turn on")):
            self.turnOn()
        if(command.startswith("turn off")):
            self.turnOff()
        if(command.startswith("toggle")):
            self.toggle()
