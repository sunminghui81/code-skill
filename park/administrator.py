
from park.select_park import *

PARK_NO_PROMPT = '&&park&&'


class Administrator(object):
    def __init__(self):
        self.parks = []

    def add_park(self, park):
        park.id = len(self.parks)
        self.parks.append(park)
        return len(self.parks)

    @property
    def park_num(self):
        return len(self.parks)

    def parking(self, car):
        index = select_park(self.parks, MODE_SEQ)
        return self.parks[index].parking(car) + PARK_NO_PROMPT + str(index)

    def taking(self, parking_id):
        park_id = int(parking_id.split(PARK_NO_PROMPT)[-1])
        uuid = parking_id.split(PARK_NO_PROMPT)[0]
        return self.parks[park_id].taking(uuid)
