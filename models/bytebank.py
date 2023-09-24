from datetime import date, datetime

def hydrate_string(string: str):
    return string.strip()

class Employee:
    def __init__(self, full_name, birth_date, salary):
        self._full_name = hydrate_string(full_name)
        self._birth_date = birth_date 
        self._salary = salary
    
    @property
    def full_name(self):
        return self._full_name
    
    @property
    def salary(self):
        return self._salary
    
    @property
    def last_name(self):
        return self._full_name.split(" ")[-1]
    
    def _is_partner(self):
        # maybe remove this
        directors_last_name = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Moura']
        return self.last_name in directors_last_name

    def decrease_salary(self):
        MAX_SALARY = 100000
        if self._salary >= MAX_SALARY and self._is_partner():
            self._salary -= self._salary * 0.1
    
    # calculate the age of the employee
    def age(self):

        def getCurrentYear():
            return date.today().year
        
        def getBirthYear():
            return int(self._birth_date.split("/")[-1])
        
        return getCurrentYear() - getBirthYear()
    
    def calculate_credits(self):
        result = self._salary * 0.1
        if result > 1000:
            raise Exception("Very high salary")
        return result

    def __str__(self):
        return f'Funcionario({self._full_name}, {self._birth_date}, {self._salary})'