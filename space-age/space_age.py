def converter(time):
    def result(self):
        return round(self.seconds / 31557600 / time, 2)

    return result


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    on_earth = converter(1)
    on_mercury = converter(0.2408467)
    on_venus = converter(0.61519726)
    on_mars = converter(1.8808158)
    on_jupiter = converter(11.862615)
    on_saturn = converter(29.447498)
    on_uranus = converter(84.016846)
    on_neptune = converter(164.79132)
