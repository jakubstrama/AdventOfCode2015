class Route():
    fromCity = None
    toCity = None
    distance = 0

    def __init__(self, fromCity, toCity, distance):
        self.fromCity = fromCity
        self.toCity = toCity
        self.distance = distance

    def __str__(self):
        return "From {0}; to: {1}; distance: {2};".format(self.fromCity, self.toCity, self.distance)
