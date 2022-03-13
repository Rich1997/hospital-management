import patient as pat
import employee as emp


def main():
    input_handler = ['', pat.add_patient, pat.view_all_patients, pat.update_patient,
                     pat.delete_patient, emp.add_employee, emp.view_all_employees, emp.update_employee, emp.delete_employee, lines]
    while True:
        try:
            lines()
            while True:
                user_input = int(input('\n--> '))
                if user_input == 10:
                    break
                if user_input > 0 and user_input < 10:
                    input_handler[user_input]()
                else:
                    print('\nInvalid input!')
            break
        except ValueError:
            print('Please input integer only...')


def lines():
    print()
    print('HOSPITAL MANAGEMENT SYSTEM')
    print('==========================')
    print(' 1. Add a new patient')
    print(' 2. View all patients')
    print(' 3. Update patient details')
    print(' 4. Delete patient')
    print(' 5. Add a new employee')
    print(' 6. View all employees')
    print(' 7. Update employee details')
    print(' 8. Delete employee')
    print(' 9. To print this list again')
    print(' 10. Exit')


if __name__ == '__main__':
    main()
