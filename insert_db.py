#Test insert data. Probably Remove later

import sqlite3
conn = sqlite3.connect('prod.db')
c = conn.cursor()

c.execute("INSERT INTO users (id, first_name, last_name) VALUES (1, 'Kleiner', 'Perkins')")

c.execute("INSERT INTO users (id, first_name, last_name) VALUES (2, 'Caulfield', 'Byers')")

c.execute("INSERT INTO courses (id, title, description) VALUES (1, 'Reproduction', 'Learning about the body.')")

c.execute("INSERT INTO courses (id, title, description) VALUES (2, 'Finance', 'Learn how to budget.')")

c.execute("INSERT INTO user_courses (user_id, course_id) VALUES (1, 1)")

c.execute("INSERT INTO user_courses (user_id, course_id) VALUES (1, 2)")

c.execute("INSERT INTO user_courses (user_id, course_id) VALUES (2, 1)")

c.execute("INSERT INTO lessons (id, title, data, image, course_id) VALUES (1, 'Male Body', 'Everything you ever wanted to know about the male body', 'http://google.com', 1)")

conn.commit()
conn.close()
