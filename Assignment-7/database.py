import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",     
    password="ansh123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade CHAR(1)
)
""")

cur.execute("TRUNCATE TABLE students;") 
cur.execute("""
INSERT INTO students (name, age, grade) VALUES
('Alice', 20, 'A'),
('Bob', 22, 'B'),
('Charlie', 19, 'C'),
('David', 21, 'A'),
('Eve', 23, 'B')
""")


conn.commit()


print("\n1. Students age > 20:")
cur.execute("SELECT * FROM students WHERE age > 20;")
print(cur.fetchall())

print("\n2. Students with grade = 'A':")
cur.execute("SELECT * FROM students WHERE grade = 'A';")
print(cur.fetchall())

print("\n3. Students with age BETWEEN 20 AND 22:")
cur.execute("SELECT * FROM students WHERE age BETWEEN 20 AND 22;")
print(cur.fetchall())

print("\n4. Students with name LIKE 'A%':")
cur.execute("SELECT * FROM students WHERE name LIKE 'A%';")
print(cur.fetchall())

print("\n5. Students with grade IN ('A','C'):")
cur.execute("SELECT * FROM students WHERE grade IN ('A','C');")
print(cur.fetchall())

cur.close()
conn.close()
