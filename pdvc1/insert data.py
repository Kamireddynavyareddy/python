import mysqlmysql.connector
dbcon=None
try:
    dbcon=mysql.connector.connect(host='localhost',)
                                    user name='rooT',
                                    password='root',
                                    database='11am'
    cursor = dbcon.cursor()
    sql_st=''''''
             insert into employee(eid,ename,esal)
             (102,"vijay",20000.0),
             (103,"sai",30000.0);
             cursor.execute(sql_st)
             dbcon.commit()
             print("data inserted succesfully")


    except mysql.connector .error as err
                                
                                print("error: ",err)
    dbcon.rollback()