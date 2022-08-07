import sqlite3
import os
from .backup import save_file
from .backup import initial_load
def connect():
    if not os.path.exists('DataBase'):
        os.mkdir('DataBase')
    conn = sqlite3.connect('DataBase/database.db')
    sql = '''CREATE TABLE IF NOT EXISTS
            User ( ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            USER_ID NOT NULL UNIQUE,
            PASSWORD BLOB NOT NULL,
            RATING FLOAT DEFAULT 0.0)'''
    conn.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS
            Path1 (ID INT PRIMARY KEY,
            TASK01 FLOAT DEFAULT 0.0, TASK02 FLOAT DEFAULT 0.0, TASK03 FLOAT DEFAULT 0.0, 
            TASK04 FLOAT DEFAULT 0.0, TASK05 FLOAT DEFAULT 0.0, TASK06 FLOAT DEFAULT 0.0,
            TASK07 FLOAT DEFAULT 0.0, TASK08 FLOAT DEFAULT 0.0, TASK09 FLOAT DEFAULT 0.0,
            TASK10 FLOAT DEFAULT 0.0,
            FOREIGN KEY (ID) REFERENCES User (ID) ON DELETE CASCADE)'''
    conn.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS
            Path2 (ID INT PRIMARY KEY,
            TASK01 FLOAT DEFAULT 0.0, TASK02 FLOAT DEFAULT 0.0, TASK03 FLOAT DEFAULT 0.0, 
            TASK04 FLOAT DEFAULT 0.0, TASK05 FLOAT DEFAULT 0.0, TASK06 FLOAT DEFAULT 0.0,
            TASK07 FLOAT DEFAULT 0.0, TASK08 FLOAT DEFAULT 0.0, TASK09 FLOAT DEFAULT 0.0,
            TASK10 FLOAT DEFAULT 0.0,
            FOREIGN KEY (ID) REFERENCES User (ID) ON DELETE CASCADE)'''
    conn.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS
            Path3 (ID INT PRIMARY KEY,
            TASK01 FLOAT DEFAULT 0.0, TASK02 FLOAT DEFAULT 0.0, TASK03 FLOAT DEFAULT 0.0, 
            TASK04 FLOAT DEFAULT 0.0, TASK05 FLOAT DEFAULT 0.0, TASK06 FLOAT DEFAULT 0.0,
            TASK07 FLOAT DEFAULT 0.0, TASK08 FLOAT DEFAULT 0.0, TASK09 FLOAT DEFAULT 0.0,
            TASK10 FLOAT DEFAULT 0.0,
            FOREIGN KEY (ID) REFERENCES User (ID) ON DELETE CASCADE)'''
    conn.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS
            Files (ID INT NOT NULL,
            PATH INT NOT NULL,
            TASK INT NOT NULL,
            FILE TEXT NOT NULL,
            FOREIGN KEY (ID) REFERENCES User (ID) ON DELETE CASCADE)'''
    conn.execute(sql)
    conn.commit()
    return conn


def create_user(conn,name,username,password):
    try:
        sql = '''INSERT INTO User (NAME,USER_ID,PASSWORD)
            VALUES ('{}','{}',"{}")'''.format(name,username,password)
        conn.execute(sql)
        conn.commit()
        initial_load(username)
        return 2
    except :
        return 4

def view_user(conn,username):
    cur = conn.cursor()
    sql='''
    SELECT * FROM User Where USER_ID = '{}'
    '''.format(username)
    return(cur.execute(sql).fetchall())

def login_user(conn,username,password):
    password = str(password)
    cur = conn.cursor()
    sql='''
    SELECT PASSWORD FROM User Where USER_ID = '{}'
    '''.format(username)
    password_crct = cur.execute(sql).fetchall()
    try:
        if password_crct[0][0] == password:
            return 1,username
        else:
            return 4,0
    except:
        return 5,0

def add_score(conn,table,username,tup_score):
    user_id = view_user(conn,username)[0][0]
    values = ('TASK01','TASK02','TASK03','TASK04','TASK05','TASK06','TASK07','TASK08','TASK09','TASK10')
    tup_score_converted = list(map(str,tup_score))
    sql= '''INSERT OR REPLACE INTO {} (ID,{}) values ({},{})'''.format( table,','.join(values),user_id,','.join(tup_score_converted))
    conn.execute(sql)
    conn.commit()
    
def update_rating(conn,table,username,rating):
    sql = '''UPDATE User SET Rating = {} Where USER_ID = "{}" '''.format(rating,username)
    conn.execute(sql)
    conn.commit()
    
def view_score(conn,username,path):
    cur = conn.cursor()
    ID = view_user(conn,username)[0][0]
    values = ('TASK01','TASK02','TASK03','TASK04','TASK05','TASK06','TASK07','TASK08','TASK09','TASK10')
    sql='''
    SELECT {} FROM {} Where ID = {}
    '''.format(','.join(values),path,ID)
    
    return(cur.execute(sql).fetchall())

def add_file_details(conn,username,file,edited=0):
    ID = view_user(conn,username)[0][0]
    file_name = save_file(file)
    sql = ''' INSERT INTO Files( ID,PATH,TASK,FILE,EDIT_FL)
            VALUES("{}","{}","{}","{}")'''.format(ID,file_name[1],file_name[3],file_name)
    conn.execute(sql)
    conn.commit()
def get_file_details(conn,username,path='',task=''):
    cur = conn.cursor()
    ID = view_user(conn,username)[0][0]
    if path and task:
        sql = '''SELECT FILE FROM Files
                Where PATH="{}" and TASK="{}" and ID="{}"'''.format(path,task,ID)
    elif path:
        sql = '''SELECT FILE FROM Files
                Where PATH="{}" and ID="{}"'''.format(path,ID)
    elif task:
        sql = '''SELECT FILE FROM Files
                Where  TASK="{}" and ID="{}"'''.format(task,ID)
    else:
        sql = '''SELECT FILE FROM Files
                Where ID="{}"'''.format(ID)
    return(cur.execute(sql).fetchall())


