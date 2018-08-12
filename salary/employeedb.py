
import abc


class EmployeeDB(object):

    @abc.abstractmethod
    def save(self, employee):
        raise TypeError('invalid implement of save method')

    @abc.abstractmethod
    def empty(self):
        raise TypeError('invalid implement of empty method')

    @property
    @abc.abstractmethod
    def num(self):
        raise TypeError('invalid implement of num method')


class HourEmployeeDB(EmployeeDB):
    DB = []

    def save(self, employee):
        if employee in HourEmployeeDB.DB:
            raise ValueError('same emplee!')
        HourEmployeeDB.DB.append(employee)

    def empty(self):
        del HourEmployeeDB.DB[:]

    @property
    def num(self):
        return len(HourEmployeeDB.DB)