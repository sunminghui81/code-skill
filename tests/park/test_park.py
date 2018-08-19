import pytest

from park.administrator import Administrator
from park.park import Park
from park.car import Car

@pytest.fixture()
def adminor():
    return Administrator()


@pytest.fixture()
def ins_park():
    return Park(5)


CAR_ID1 = u'沪A 123456'


@pytest.fixture()
def car():
    return Car(CAR_ID1)

def test_adminor_add_park(adminor, ins_park):
    assert adminor.add_park(ins_park) == 1

def test_adminor_parking(adminor, car, ins_park):
    adminor.add_park(ins_park)
    assert adminor.parking(car)

def test_adminor_taking(adminor, car, ins_park):
    adminor.add_park(ins_park)
    park_id = adminor.parking(car)
    assert adminor.taking(park_id).car_id == CAR_ID1
