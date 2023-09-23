from models.bytebank import Employee 

class TestBytebank:
    def test_age_when_input_is_valid(self):
        employee = Employee('John', '11/11/2000', 1000)
        assert employee.age() == 23

    def test_calculate_credits(self):
        employee = Employee('John', '11/11/2000', 1000)
        assert employee.calculate_credits() == 100

    def test_get_last_name(self):
        employee = Employee('John Doe', '11/11/2000', 1000)
        assert employee.last_name == "Doe"

    def test_salary_decrease_when_receive_100000_return_90000(self):
        # arrange
        input_salary = 100000
        input_name = 'Ciro Moura'
        result = 90000

        employee = Employee(input_name, '11/11/2000', input_salary)
        employee.decrease_salary() # act

        assert employee.salary == result # assert