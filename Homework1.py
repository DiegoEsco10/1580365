import mysql.connector
from mysql.connector import Error


def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=userpw,
            database=dbname
        )
    except Error as e:
        print(f'the error {e} occured')
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed succesfully")
    except Error as e:
        print(f"The error '{e}' occured.")


def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occured")


# creating connection to mysql database
conn = create_con('test1.cogsvkqpg7tp.us-east-2.rds.amazonaws.com', 'DiegoE', 'password', 'test1db')
cursor = conn.cursor()


def show_menu():
    print("a - Add car")
    print("d - Remove car")
    print("u - Update car details")
    print("r1 - Output all cars sorted by year (ascending)")
    print("r2 - Output all cars of a certain color")
    print("q- Quit")


def add_car():
    car_make = input('Enter car make:')
    car_model = input('Enter car model:')
    car_year = int(input('Enter year of car:'))
    car_color = input('Enter car color:')
    cursor.execute("INSERT INTO Garage (make, model, year, color) VALUES ('%s', '%s', '%s', '%s')" %
                   (car_make, car_model, car_year, car_color))
    conn.commit()
    query = 'SELECT * FROM Garage WHERE id=(SELECT max(id) FROM Garage)'
    cursor.execute(query,)
    print('New Record added:')
    for i in cursor:
        print(i)


def remove_car():
    cursor.execute('SELECT * FROM Garage')
    for i in cursor:
        print(i)
    id = input('Enter ID to Delete:')
    query = 'DELETE FROM Garage WHERE id = %s'
    data = (id,)
    cursor.execute(query, data)
    conn.commit()
    print("Total rows deleted: %d" % cursor.rowcount)


def update_car_make(id):
    query = "SELECT * FROM Garage WHERE id = %s "
    data = (id,)
    cursor.execute(query, data)
    for i in cursor:
        print(i)
    car_make = input('Enter new car Make:')
    query = "UPDATE Garage SET make ='\{}\' WHERE id = '\{}\' ".format(car_make, id)
    cursor.execute(query)
    print("Total rows updated: %d" % cursor.rowcount)
    query = 'SELECT * FROM Garage WHERE id = %s '
    data = (id,)
    cursor.execute(query, data)
    print('Updated Record:')
    for i in cursor:
        print(i)
    conn.commit()


def update_car_model(id):
    query = 'SELECT * FROM Garage WHERE id = %s '
    data = (id,)
    cursor.execute(query, data)
    for i in cursor:
        print(i)
    car_model = input('Enter new car Model:')
    query = "UPDATE Garage SET model ='{}' WHERE id = '\{}\' ".format(car_model, id)
    cursor.execute(query)
    print("Total rows updated: %d" % cursor.rowcount)
    query = 'SELECT * FROM Garage WHERE id = %s '
    data = (id,)
    cursor.execute(query, data)
    print('Updated Record:')
    for i in cursor:
        print(i)
    conn.commit()


def update_car_year(id):
    query = "SELECT * FROM Garage WHERE id = %s "
    data = (id,)
    cursor.execute(query, data)
    for i in cursor:
        print(i)
    car_year = int(input('Enter new car Year:'))
    if type(car_year) == int or type(car_year) == float:
        query = "UPDATE Garage SET year ='\{}\' WHERE id = '\{}\' ".format(car_year, id)
        cursor.execute(query)
        print("Total rows updated: %d" % cursor.rowcount)
        query = 'SELECT * FROM Garage WHERE id = %s '
        data = (id,)
        cursor.execute(query, data)
    else:
        print('The variable is not a number')
        return
    print('Updated Record:')
    for i in cursor:
        print(i)
    conn.commit()


def update_car_color(id):
    query = "SELECT * FROM Garage WHERE id = %s "
    data = (id,)
    cursor.execute(query, data)
    for i in cursor:
        print(i)
    car_color = input('Enter new car color:')
    query = "UPDATE Garage SET color ='{}' WHERE id = '\{}\' ".format(car_color, id)
    cursor.execute(query)
    print("Total rows updated: %d" % cursor.rowcount)
    query = 'SELECT * FROM Garage WHERE id = %s '
    data = (id,)
    cursor.execute(query, data)
    print('Updated Record:')
    for i in cursor:
        print(i)
    conn.commit()


def update_car_all(id):
    query = "SELECT * FROM Garage WHERE id = %s "
    data = (id,)
    cursor.execute(query, data)
    for i in cursor:
        print(i)
    car_make = input('Enter new car make:')
    car_model = input('Enter new car model:')
    car_year = input('Enter new car year:')
    car_color = input('Enter new car color:')
    query = "UPDATE Garage SET make ='\{}\', model ='{}',year ='\{}\' ,color ='{}' WHERE id = '\{}\' ".format(
        car_make, car_model, car_year, car_color, id)
    cursor.execute(query)
    print("Total rows updated: %d" % cursor.rowcount)
    query = 'SELECT * FROM Garage WHERE id = %s '
    data = (id,)
    cursor.execute(query, data)
    print('Updated Record:')
    for i in cursor:
        print(i)
    conn.commit()


def update_car_menu():
    cursor.execute('SELECT * FROM Garage')
    for i in cursor:
        print(i)
    id = input('Enter ID to update:')
    query = 'SELECT * FROM Garage WHERE id = %s '
    data = (id,)
    cursor.execute(query, data)
    for i in cursor:
        print(i)
    while True:
        print("1 - Update Make of vehicle ")
        print("2 - Update Model of vehicle")
        print("3 - Update car year")
        print("4 - Update car color")
        print("5 - Update Make, Model, Year, Color ")
        choice = input("Enter your choice(Type 'b' to go back to Main Menu:").lower()
        if choice == "b":
            print("Back to main menu")
            return
        elif choice == "1":
            update_car_make(id)
        elif choice == "2":
            update_car_model(id)
        elif choice == "3":
            update_car_year(id)
        elif choice == "4":
            update_car_color(id)
        elif choice == "5":
            update_car_all(id)
        else:
            print("That is not a valid choice. You can only choose from the menu.")


def sorted_car():
    cursor.execute('SELECT * FROM Garage ORDER BY year ASC ')
    for i in cursor:
        print(i)


def sorted_by_color():
    cursor.execute('SELECT DISTINCT color FROM Garage')
    for i in cursor:
        print(i)
    user_color_pick = input('Please enter color:')
    if type(user_color_pick) == str:
        query = "SELECT * FROM Garage WHERE color = '\{}\'".format(user_color_pick)
        cursor.execute(query,)
        for i in cursor:
            print(i)
    else:
        print('The Color entered does not exist. Please ENTER a color that exist. ')
        return
    conn.commit()


def menu():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        show_menu()
        choice = input("Enter your choice: ").lower()
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return
        elif choice == "a":
            add_car()
        elif choice == "d":
            remove_car()
        elif choice == "u":
            update_car_menu()
        elif choice == "r1":
            sorted_car()
        elif choice == "r2":
            sorted_by_color()
        else:
            print("That is not a valid choice. You can only choose from the menu.")


if __name__ == "__main__":
    menu()
