from database import get_connection
from models import Student

# Function 1 --- add_student

def add_student(std_name, age, standard, guard_c_no):

    connection = get_connection()

    if connection is None:
        print("Database Connection Failed.")
        return

    cursor = connection.cursor()

    query = """
    INSERT INTO students
    (std_name, age, standard, guard_c_no)
    VALUES (%s,%s,%s,%s)
    """

    values = (
        std_name,
        age,
        standard,
        guard_c_no
    )

    try:

        cursor.execute(query, values)

        connection.commit()

        print("\nStudent Registered Successfully.")

    except Exception as e:

        print("Error :", e)

    finally:

        cursor.close()
        connection.close()

# Function 2 --- view_all_students

def view_all_students():

    connection = get_connection()

    if connection is None:
        print("Database Connection Failed.")
        return

    cursor = connection.cursor()

    query = "SELECT * FROM students"

    try:

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:

            print("\nNo Student Records Found.")

            return

        print("\nStudent Records")
        print("-"*60)

        for row in records:

            student = Student(*row)

            student.display()

            print("-"*60)

    except Exception as e:

        print("Error :", e)

    finally:

        cursor.close()

        connection.close()

# Function 3 --- search_student

def search_student(student_id):

    connection = get_connection()

    if connection is None:
        print("Database Connection Failed.")
        return

    cursor = connection.cursor()

    query = """
    SELECT *
    FROM students
    WHERE std_id=%s
    """

    try:

        cursor.execute(query, (student_id,))

        record = cursor.fetchone()

        if record:

            student = Student(*record)

            student.display()

        else:

            print("\nStudent Not Found.")

    except Exception as e:

        print("Error :", e)

    finally:

        cursor.close()

        connection.close()

# Function 4 --- Update Standard

def update_standard(student_id, new_standard):

    connection = get_connection()

    if connection is None:
        print("Database Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        # Check if student exists
        cursor.execute(
            "SELECT * FROM students WHERE std_id=%s",
            (student_id,)
        )

        record = cursor.fetchone()

        if not record:
            print("\nStudent Not Found.")
            return

        # Update standard
        cursor.execute(
            """
            UPDATE students
            SET standard=%s
            WHERE std_id=%s
            """,
            (new_standard, student_id)
        )

        connection.commit()

        print("\nStandard Updated Successfully.")

    except Exception as e:

        print("Error :", e)

    finally:

        cursor.close()
        connection.close()

# Function 5 --- update_contact

def update_contact(student_id, new_contact):

    connection = get_connection()

    if connection is None:
        print("Database Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        # Check if student exists
        cursor.execute(
            "SELECT * FROM students WHERE std_id=%s",
            (student_id,)
        )

        record = cursor.fetchone()

        if not record:
            print("\nStudent Not Found.")
            return

        # Update Contact Number
        cursor.execute(
            """
            UPDATE students
            SET guard_c_no=%s
            WHERE std_id=%s
            """,
            (new_contact, student_id)
        )

        connection.commit()

        print("\nGuardian Contact Updated Successfully.")

    except Exception as e:

        print("Error :", e)

    finally:

        cursor.close()
        connection.close()

# Function 6 --- delete_student

def delete_student(student_id):

    connection = get_connection()

    if connection is None:
        print("Database Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        # Check if student exists
        cursor.execute(
            "SELECT * FROM students WHERE std_id=%s",
            (student_id,)
        )

        record = cursor.fetchone()

        if not record:
            print("\nStudent Not Found.")
            return

        # Delete Student
        cursor.execute(
            """
            DELETE FROM students
            WHERE std_id=%s
            """,
            (student_id,)
        )

        connection.commit()

        print("\nStudent Deleted Successfully.")

    except Exception as e:

        print("Error :", e)

    finally:

        cursor.close()
        connection.close()