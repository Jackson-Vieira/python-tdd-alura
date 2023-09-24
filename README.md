# PYTHON-TDD-ALURA

## What is TDD 
<!-- imagem representando tdd centralizada -->
![TDD](https://imgs.search.brave.com/4A2sanGm7OzwY_qem7_4uHX6bAhEIqxfkQZnF_a0B9I/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9ka3Ju/NHNrMHJuMzF2LmNs/b3VkZnJvbnQubmV0/LzIwMTkvMTEvMDQx/MDUwMjAvaW1nLXRk/ZC5wbmc)

O TDD é uma técnica de desenvolvimento de software que consiste em escrever testes antes de escrever o código de produção. O objetivo é garantir que o código de produção seja escrito apenas para passar nos testes, ou seja, que o código de produção seja escrito apenas para atender aos requisitos do teste.

1. Escrever um teste que falhe
2. Escrever o código que faça o teste passar
3. Refatorar o código
4. Repetir

O TDD e de extrema importancia por que os testes testam as regras de negocio e a logica do codigo, e o codigo é escrito para passar nos testes, ou seja, o codigo é escrito para atender aos requisitos do teste.


### Example

Nosso chefe pediu para desenvolver uma feature para um sistema de banco chamado bitebank. a tarefa consiste em desenvolver uma classe chamada `Employee` que tenha os atributos `name`, `salary` e `role`. O atributo `role` deve ser um atributo privado e os outros dois atributos devem ser públicos. O atributo `role` deve ser do tipo `str` e os outros dois atributos devem ser do tipo `float`. O atributo `role` deve ser inicializado com o valor `Developer` e os outros dois atributos devem ser inicializados com o valor `None`. A classe deve ter um método chamado `increase_salary` que deve aumentar o salário do funcionário em 10%. O método deve retornar o salário após o aumento. O método deve ser testado.


make a test that fails
```python
```python
class TestEmployee:
    def test_create_employee(self):
        employee = Employee("Jhon", 1000)
        assert employee.name is "Jhon"
        assert employee.salary is 1000
        assert employee._role == 'Developer'

    def test_increase_salary(self):
        employee = Employee()
        employee.salary = 1000
        assert employee.increase_salary() == 1100
```

make the code that makes the test pass

```python
class Employee:
    def __init__(self, name=None, salary=None):
        self.name = name
        self.salary = salary
        self._role = 'Developer'

    def increase_salary(self):
        self.salary = self.salary * 1.1
        return self.salary
```

refactor the code

```python
class Employee:
    DEFAULT_ROLE = 'Developer'
    
    def __init__(self, name=None, salary=None):
        self.name = name
        self.salary = salary
        self._role = Employee.DEFAULT_ROLE

    def increase_salary(self):
        if self.salary is not None and self.salary >= 0:
            self.salary += self.salary * (percentage_increase / 100)
            return self.salary
        else:
            raise ValueError("Salary must be a non-negative number")
    
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role
```

repeat the process (improve tests)

```python
import pytest

class TestEmployee:
    def test_create_employee(self):
        employee = Employee("Jhon", 1000)
        assert employee.name is "Jhon"
        assert employee.salary is 1000
        assert employee.role == 'Developer'

    def test_increase_salary(self):
        employee = Employee()
        employee.salary = 1000
        assert employee.increase_salary() == 1100

    def test_increase_salary_with_negative_salary(self):
        employee = Employee()
        employee.salary = -1000
        with pytest.raises(ValueError):
            employee.increase_salary()
```


## Pytest and Pytest-cov Commands

### pytest

```bash
pytest -v
```

This command will run all tests in the project the `-v` flag will show the tests results in a verbose way, 
means that the command will show the tests results in a more detailed way.

### pytest-cov

```bash
pytest --cov=models
```

This command will run all tests in the project and will show the test coverage of the project.

### Reports with pytest-cov

```bash
pytest --cov=models --cov-report=html
```

This command will run all tests in the project and will show the test coverage of the project in a html report.

```bash
pytest --cov=models --cov-report=term-missing
```

This command will run all tests in the project and will show the test coverage of the project in a terminal report.

```bash
pytest --cov=models --cov-report=xml
```

This command will run all tests in the project and will show the test coverage of the project in a xml report.


## Pytest and Pytest-cov Configuration

### pytest.ini 
    ```ini
    [pytest]
    addopts = -v --cov=models /tests --cov-report=term-missing
    ```
### .coveragerc
    ```ini
    [run]
    source = models
    omit = */__init__.py
    ```

## Run Tests

```bash
pytest
```