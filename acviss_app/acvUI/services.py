import mysql.connector
import string
import random
from django.shortcuts import redirect


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def populateDB(number, batch_name):
    print('inside populate')
    sql = "INSERT INTO codes (batch_name, code) VALUES (%s, %s)"
    dbconnect = mysql.connector.connect(host='localhost', port='3306', user='raun', passwd='root', database='avcissdb')
    cursor = dbconnect.cursor(buffered=True)
    for i in range(number):
        code = id_generator()
        val = (batch_name, code)
        cursor.execute(sql, val)
        dbconnect.commit()
    print('populate complete')
    return redirect('/')

def register_batch_update(name, batch_code):
    sql = "INSERT INTO batch (batch_name, user_name) VALUES (%s, %s)"
    dbconnect = mysql.connector.connect(host='localhost', port='3306', user='raun', passwd='root', database='avcissdb')
    cursor = dbconnect.cursor()
    val = (batch_code,name)
    cursor.execute(sql,val)
    dbconnect.commit()

def load_user_table(user):
    dbconnect = mysql.connector.connect(host='localhost', port='3306', user='raun', passwd='root', database='avcissdb')
    cursor = dbconnect.cursor()
    cursor.execute('select distinct  codes.batch_name, code from batch,codes where batch.user_name= %s ;', (user,))
    result = cursor.fetchall()
    dbconnect.commit()
    return result
