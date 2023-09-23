from models.bytebank import Employee 
import pytest

class TestBytebank:
    def test_age_when_input_is_valid(self):
        employee = Employee('John', '11/11/2000', 1000)
        assert employee.age() == 23

    @pytest.mark.calculate_credits 
    def test_calculate_credits(self):
        employee = Employee('John', '11/11/2000', 1000)
        assert employee.calculate_credits() == 100

    @pytest.mark.calculate_credits 
    def test_calculate_credits_if_salary_is_20000_should_return_exception(self):
        with pytest.raises(Exception):
            salary = 20000
            employee = Employee('John', '11/11/2000', salary)
            assert employee.calculate_credits()

    def test_get_last_name(self):
        employee = Employee('John Doe', '11/11/2000', 1000)
        assert employee.last_name == "Doe"

    # test if the employee is a partner and salary >= 100000 decrease 10%
    def test_partner_salary_decrease_when_receive_100000_return_90000(self):
        # arrange
        input_salary = 100000
        input_name = 'Ciro Moura'
        result = 90000

        partner = Employee(input_name, '11/11/2000', input_salary)
        partner.decrease_salary() # act

        assert partner.salary == result # assert
    
    def test_member_salary_decrease_when_receive_100000_return_10000(self):
        input_salary = 100000
        input_name = 'Jhon Doe'
        result = 100000

        partner = Employee(input_name, '11/11/2000', input_salary)
        partner.decrease_salary() # act

        assert partner.salary == result # assert
    