import sqlite3
conn = sqlite3.connect('prod.db')
c = conn.cursor()

# users
c.execute('''CREATE TABLE IF NOT EXISTS users
    (id integer primary key,
    first_name text,
    last_name text)''')

# courses
c.execute('''CREATE TABLE IF NOT EXISTS courses
    (id integer primary key,
     title text,
     description text)''')

# user_courses
c.execute('''CREATE TABLE IF NOT EXISTS user_courses
    (user_id integer,
    course_id integer,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(course_id) REFERENCES courses(id))''')

# lessons
c.execute('''CREATE TABLE IF NOT EXISTS lessons
    (id integer primary key,
    title text,
    data text,
    course_id integer,
    FOREIGN KEY(course_id) REFERENCES courses(id))''')

# quizzes
c.execute('''CREATE TABLE IF NOT EXISTS quizzes
    (id integer primary key,
    question text,
    answer_choices text,
    answer text,
    course_id integer, FOREIGN KEY(course_id) REFERENCES courses(id))''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
conn.close()
