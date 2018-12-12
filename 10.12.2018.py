import pymysql.cursors
#1

connection = pymysql.connect(host='localhost',
    user ='root',
    password='',
    db='employees',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)


try:
    with connection.cursor() as cursor:
        sql = 'SELECT first_name, last_name, gender, birth_date, title FROM employees JOIN titles ON employees.emp_no = titles.emp_no'
        a = cursor.execute(sql, )
        res = cursor.fetchall()
        print (res)

finally:
    connection.close()

        

#2 
connection = pymysql.connect(host='localhost',
    user ='root',
    password='',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = 'CREATE TABLE db.new_employees SELECT first_name, last_name, gender, birth_date, title FROM employees.employees JOIN employees.titles ON employees.emp_no = titles.emp_no'
        cursor.execute(sql, )
    connection.commit()

    with connection.cursor() as cursor:
        sql = 'SELECT * FROM db.new_employees WHERE title = %s'
        cursor.execute(sql, ('Engineer',))
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()