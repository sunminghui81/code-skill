
from uuid import uuid4 as UUID




class Park(object):
    def __init__(self, num):
        self.cars = {}
        self.container_num = num

    def parking(self, car):
        uuid = UUID().__str__()
        self.cars.update({uuid : car})
        return uuid

    @property
    def residual(self):
        return self.container_num - len(self.cars)

    def has_car(self, paking_id):
        return paking_id in self.cars.keys()

    def taking(self, paking_id):
        return self.cars.pop(paking_id)

    @property
    def vacancy_rate(self):
        return self.residual / self.container_num


