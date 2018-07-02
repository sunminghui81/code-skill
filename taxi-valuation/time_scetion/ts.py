import time


class SectionHour24(object):
    def __init__(self, low, up, inner=True):
        iself._set_section(low, up)
        self.__inner = inner

    def is_valid_hour_24(self, h):
        if h > 23.99 or h < 0:
            raise Exception('hour(%d) not hour 24' % h)

    def is_in(self, h):
        self.is_valid_hour_24(h)
        if h > self.__up or h < self.__low:
            return False == self.__inner
        return True == self.__inner

    def _set_section(self, low, up):
        self.is_valid_hour_24(low)
        self.is_valid_hour_24(up)
        if low > up:
            raise Exception('section not valid!')
        self.__low = low
        self.__up = up


class Time(object):
    def __init__(self):
        self.day = SectionHour24(6.0, 23.0, inner=True)
        self.night = SectionHour24(6.0, 23.0, inner=False)
        # self.busy_1 = SectionHour24(8.0, 9.5, inner=True)
        # self.busy_2 = SectionHour24(16.5, 18.5, inner=True)

    @property
    def hour(self):
        return time.localtime().tm_hour + time.localtime().tm_min/60

