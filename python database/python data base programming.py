import pymysql##### for import to use
con=pymysql.connect()### for connectoion (user name /passward)
curser=con.cursor()## for writing oject
curser.execute()
curser.executemany()
curser.executescript()
curser.fetchone()
curser.fetchmany()
curser.fetchall()
commite()
roolback()
con.commit()
con.rollback()
con.close()
curser.close()






import cx_Oracle ##### for import to use
con=cx_Oracle.connect('scott/tiger@localhost')### for connectoion (user name /passward)
curser=con.cursor()## for writing oject
curser.execute()
curser.executemany()
curser.executescript()
curser.fetchone()
curser.fetchmany()
curser.fetchall()
commite()
roolback()
con.commit()
con.rollback()
con.close()
curser.close()