from datetime import date, datetime

def stringToDate(date):
    return datetime.strptime(date, "%m/%d/%Y")


class Employee:
    def __init__(self, name, birth_date, salary):
        self._name = name
        self._birth_date = stringToDate(birth_date)
        self._salary = salary 

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary
    
    # calculate the age of the employee
    def age(self):
        def getCurrentYear():
            return date.today().year
        return getCurrentYear() - self._birth_date.year
    
    def calculate_credits(self):
        result = self._salary * 0.1
        if result > 1000:
            result = 0
        return result

    def __str__(self):
        return f'Funcionario({self._name}, {self._birth_date}, {self._salary})'