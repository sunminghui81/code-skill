import pytest


from salary.employee import FactoryEmploy
from salary.employeedb import HourEmployeeDB

@pytest.fixture()
def hour_employ_info():
    return {'empid': '1', 'name': 'bob', 'addr': 'xidu', 'kind': 'hour', 'rate': 50}

@pytest.fixture()
def setup():
    return HourEmployeeDB().empty()

@pytest.fixture()
def hour_employ():
    return FactoryEmploy().instance('hour')

def test_hour_employee(hour_employ_info, hour_employ):
    hour_employ.add(**hour_employ_info)
    assert hour_employ.num == 1

#
# def test_hour_employee_submit(hour_employ_info):
#     Employee().add(**hour_employ_info)
#     EmployeeApp().submit()


