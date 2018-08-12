import abc

from salary.employeedb import HourEmployeeDB




class Employee(object):
    def __init__(self):
        self.empid = ''
        self.name = ''
        self.addr = ''
        self.salary = 0
        self.db = None

    def init(self, **kwargs):
        self.person_info(**kwargs)
        self.career_info(**kwargs)

    @abc.abstractmethod
    def career_info(self, **kwargs):
        raise TypeError('invalid implement of career_info method')

    def person_info(self, **kwargs):
        self.empid = kwargs['empid']
        self.name = kwargs['name']
        self.addr = kwargs['addr']

    def add(self, **kwargs):
        self.init(**kwargs)
        self.db.save(self)

    @property
    def num(self):
        return self.db.num


class HourEmployee(Employee):
    def __init__(self):
        super(HourEmployee, self).__init__()
        self.kind = ''
        self.rate = 0
        self.db = HourEmployeeDB()

    def career_info(self, **kwargs):
        self.kind = kwargs['kind']
        self.rate = kwargs['rate']

class FactoryEmploy(object):
    def __init__(self):
        pass

    def instance(self, kind):
        return {'hour': HourEmployee}[kind]()

