class Santa:
    x = 0
    y = 0

    up = '^'
    down = 'v'
    left = '<'
    right = '>'

    def __init__(self, houses):
        self.houses = houses
        self._updateDict()

    def move(self, direction):
        if(direction == self.up):
            self.y += 1
        elif(direction == self.down):
            self.y -= 1
        elif(direction == self.right):
            self.x += 1
        elif(direction == self.left):
            self.x -= 1

        self._updateDict()


    def _getLocation(self):
        return (self.x, self.y)

    def _updateDict(self):
        key = self._getLocation()
        if(key in self.houses):
            self.houses[key] += 1
        else:
            self.houses[key] = 1
