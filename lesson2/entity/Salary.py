import re


class Salary:
    """
    Заплата
    """

    def __init__(self, salary: str):
        if not (salary and (not salary.isspace())):
            self.__start = 0
            self.__end = 0

        self.__convert_to_salary(salary)

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value: float):
        self.__start = value

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, value: float):
        self.__end = value

    def __repr__(self):
        return f"{self.__start} - {self.__end}"

    def __convert_to_salary(self, value: str):
        """
        Конвертация строки в from to
        """
        if value == '' or not self.has_numbers(value):
            self.__start = 0
            self.__end = 0
            return

        split_value = value.split('-')
        self.__start = int(re.sub('\D', '', split_value[0]))
        self.__end = int(re.sub('\D', '', split_value[1])) if len(split_value) > 1 else 0

    def has_numbers(self, value: str):
        return any(char.isdigit() for char in value)
