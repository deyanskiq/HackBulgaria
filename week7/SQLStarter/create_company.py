import sqlite3
# from manage_company import commands


connection = sqlite3.connect("company.db")
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS
company(id INTEGER PRIMARY KEY,name TEXT
    ,monthly_salary  INTEGER,yearly_bonus INTEGER,position TEXT)
  """
cursor.execute(create_table_query)
cursor.execute("""INSERT INTO company(name,monthly_salary,yearly_bonus,position)
VALUES ("Ivan Ivanov ",5000,10000,"Software Developer"),
("Rado Rado",500,0,"Technical Support Intern"),
("Ivo Ivo ",10000,100000,"CEO"),
("Petar Petrov ",3000,1000,"Marketing Manager"),
("Maria Georgieva ",8000,10000,"COO")
""")

connection.commit()
