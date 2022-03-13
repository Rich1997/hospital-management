import mysql.connector


def add_employee():
    cnx = mysql.connector.connect(user='Rich', password='1234', host='127.0.0.1', database='hospital_db')
    cursor = cnx.cursor()
    query = ("INSERT INTO employee (emp_id, department_id, birth_date, first_name, last_name, gender, hire_date, salary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
    while True:
        try:
            emp_id = int(input('\nEnter employee ID: '))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    while True:
        try:
            department_id = int(input('Enter department ID: '))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    birth_date = input('Enter employee birth date (use YYYY-MM-DD format): ')
    first_name = input('Enter employee first name: ')
    last_name = input('Enter employee last name: ')
    gender = input('Enter M or F for gender: ')
    hire_date = input('Enter employee hire date (use YYYY-MM-DD format): ')
    salary = input('Enter employee salary: ')
    data = (emp_id, department_id, birth_date, first_name, last_name, gender, hire_date, salary)
    cursor.execute(query, data)
    cnx.commit()
    print('\nEmployee added successfully!')
    cnx.close()


def view_all_employees():
    cnx = mysql.connector.connect(user='Rich', password='1234', host='127.0.0.1', database='hospital_db')
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM employee")
    query = cursor.fetchall()
    print('\nEmployee ID\tDepartment ID\tBirth Date\tFirst Name\tLast Name\tGender\tHire Date\tSalary')
    for (emp_id, department_id, birth_date, first_name, last_name, gender, hire_date, salary) in query:
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<7} {:<15} {:<15}".format(
            emp_id, department_id, str(birth_date), first_name, last_name, gender, str(hire_date), salary))
    cnx.close()


def update_employee():
    cnx = mysql.connector.connect(user='Rich', password='1234', host='127.0.0.1', database='hospital_db')
    cursor = cnx.cursor()
    while True:
        try:
            id = int(input('\nEnter employee ID: '))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    while True:
        try:
            department_id = int(input('Enter department ID: '))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    birth_date = input('Enter employee birth date (use YYYY-MM-DD format): ')
    first_name = input('Enter employee first name: ')
    last_name = input('Enter employee last name: ')
    gender = input('Enter M or F for gender: ')
    hire_date = input('Enter employee hire date (use YYYY-MM-DD format): ')
    salary = input('Enter employee salary: ')
    query = ("UPDATE employee SET department_id=%s, birth_date=%s, first_name = %s, last_name = %s, gender = %s, hire_date = %s, salary = %s WHERE emp_id = %s")
    data = (department_id, birth_date, first_name, last_name, gender, hire_date, salary, id)
    cursor.execute(query, data)
    cnx.commit()
    if cursor.rowcount == 0:
        print('ID not found!')
    else:
        print('\nEmployee updated successfully!')
    cnx.close()


def delete_employee():
    cnx = mysql.connector.connect(user='Rich', password='1234', host='127.0.0.1', database='hospital_db')
    cursor = cnx.cursor()
    while True:
        try:
            id = int(input('\nEnter employee ID: '))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    query = ("DELETE FROM employee WHERE emp_id = %s")
    data = (id,)
    cursor.execute(query, data)
    cnx.commit()
    if cursor.rowcount == 0:
        print('ID not found!')
    else:
        print('\nEmployee deleted successfully!')
    cnx.close()
