from connect_mysql import connect_database

#adds members to the Members table
def add_member(name, age):
    query = "INSERT INTO Members (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))

#adds workout sessions to the WorkoutSessions table
def add_workout_session(cursor, member_id, date, duration_minutes, calories_burned):
    query = """
    INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (member_id, date, duration_minutes, calories_burned))

#updates members age in the Members table
def update_member_age(new_age, member_id):
    query = """
    UPDATE Members
    SET age = %s
    WHERE id = %s
    """
    cursor.execute(query, (member_id, new_age))

    print("Member's age has been updated.")

#deletes sessions from the WorkoutSessions table
def delete_workout_session(session_id):
    query = """
    DELETE FROM WorkoutSessions
    WHERE session_id = %s
    """

    cursor.execute(query, session_id)

#retrieves members data between the given age range
def get_members_in_age_range(start_age, end_age):
    query = """
    SELECT * FROM Members
    WHERE age BETWEEN %s and %s
    """

    cursor.execute(query, (start_age, end_age))

    for row in cursor.fetchall():
        print(row)

#variable for establishing a connection to MySQL database
conn = connect_database()
#if the connection is established correctly, run the given code and commit to the database
if conn is not None:
    try:
        #create a cursor variable to execute queries in each function
        cursor = conn.cursor()

        add_member("Jimmy Wells", "33")
        update_member_age("4", "27")
        delete_workout_session(["6"])
        get_members_in_age_range("25", "30")

        #commit changes
        conn.commit()

    #ensure the cursor and connection is closed after the program has finished
    finally:
        cursor.close()
        conn.close()