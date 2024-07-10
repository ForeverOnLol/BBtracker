import datetime


class Storage():
    def __init__(self, last_update: datetime = None, common_counter: int = 0, hour_counter: int = 0):
        self.common_counter = common_counter
        self.hour_counter = hour_counter
        self.last_update = datetime.datetime.now()
        self.fresh_data = False

    def update(self):
        self.fresh_data = True
        self.hour_counter += 1
        self.common_counter += 1
        self.last_update = datetime.datetime.now()

    def get(self) -> tuple:
        self.fresh_data = False
        self.__check_overdue()
        return self.common_counter, self.hour_counter

    def __reset_hour_counter(self):
        self.hour_counter = 0

    def __check_overdue(self) -> bool:
        now = datetime.datetime.now()
        if now.hour != self.last_update.hour:
            self.hour_counter = 0
