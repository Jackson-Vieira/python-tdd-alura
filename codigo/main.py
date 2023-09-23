from bytebank import Employee 

def main():
    employee = Employee('Joao', '11/11/2005', 1000)
    print(employee)
    print(employee.age())
    print(employee.calculate_credits())

if __name__ == '__main__':
    main()