import mysql.connector


def add_patient():
    cnx = mysql.connector.connect(user='Rich', password='1234', host='127.0.0.1', database='hospital_db')
    cursor = cnx.cursor()
    query = ("INSERT INTO patient (pat_no,first_name,last_name,appointment_date,discharged,assigned_doctor_id) VALUES (%s,%s,%s,%s,%s,%s)")
    while True:
        try:
            id = int(input('\nEnter patient ID: '))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    first_name = input('Enter patient first name: ')
    last_name = input('Enter patient last name: ')
    appoint_date = input('Enter patient appointment date (use YYYY-MM-DD format): ')
    discharged = input('Enter Y or N for discharged: ')
    while True:
        try:
            doctor_id = int(input('Enter doctor ID: '))
            break
        except ValueError:
            print("Please input integer only...")
            continue

    data = (id, first_name, last_name, appoint_date, discharged, doctor_id)
    cursor.execute(query, data)
    cnx.commit()
    print('\nPatient added successfully!')
    cnx.close()


def view_all_patients():
    cnx = mysql.connector.connect(user='Rich', password='1234', host='127.0.0.1', database='hospital_db')
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM patient")
    query = cursor.fetchall()
    print('\nPatient ID\tFirst Name\tLast Name\tAppointment Date\tDischarged\tDoctor ID')
    for (pat_no, first_name, last_name, appointment_date, discharged, assigned_doctor_id) in query:
        print("{:<15} {:<15} {:<15} {:<23} {:<15} {:<15}".format(
            pat_no, first_name, last_name, str(appointment_date), discharged, assigned_doctor_id))
    cnx.close()


def update_patient():
    cnx = mysql.connector.connect(user='Rich', password='1234', host='127.0.0.1', database='hospital_db')
    cursor = cnx.cursor()
    while True:
        try:
            id = int(input('\nEnter patient ID: '))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    first_name = input('Enter patient first name: ')
    last_name = input('Enter patient last name: ')
    appointment_date = input('Enter patient appointment date (use YYYY-MM-DD format): ')
    discharged = input('Enter Y or N for discharged: ')
    while True:
        try:
            doctor_id = int(input('Enter doctor ID: '))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    query = ("UPDATE patient SET first_name = %s, last_name = %s, appointment_date = %s, discharged = %s, assigned_doctor_id = %s WHERE pat_no = %s")
    data = (first_name, last_name, appointment_date, discharged, doctor_id, id)
    cursor.execute(query, data)
    cnx.commit()
    if cursor.rowcount == 0:
        print('ID not found!')
    else:
        print('\nPatient updated successfully!')
    cnx.close()


def delete_patient():
    cnx = mysql.connector.connect(user='Rich', password='1234', host='127.0.0.1', database='hospital_db')
    cursor = cnx.cursor()
    while True:
        try:
            id = int(input('\nEnter patient ID: '))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    query = ("DELETE FROM patient WHERE pat_no = %s")
    data = (id,)
    cursor.execute(query, data)
    cnx.commit()
    if cursor.rowcount == 0:
        print('ID not found!')
    else:
        print('\nPatient deleted successfully!')
    cnx.close()
