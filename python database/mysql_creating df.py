import mysql
import mysql.connector
cour=mysql.connector.connect(user="root",password="1234",db="mydb",host="localhost")
cr=cour.cursor()
cr.execute("show databases")
cr.fetchall()
cr.execute("show tables")
cr.fetchall()
cr.execute("select *  from employes")
cr.fetchall()
c=cr.fetchall()
import pandas as pd
import numpy as np
da=pd.DataFrame(c,index=np.arange(7))
df=da.iloc[:,1:]
df
df["new"]=1
df
cr.execute("select * from employes where age=34")
cr.fetchall()
cr.execute("insert into employes values(18,'shiva','f',23,123213)")
cr.fetchall()
cr.close()
cour.close()
cour.commit()
