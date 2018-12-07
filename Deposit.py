#!C:\Users\Shyam\AppData\Local\Programs\Python\Python36\python.exe
import cgi, cgitb 
import cx_Oracle
form = cgi.FieldStorage() 
users = form.getvalue('user')
print ("Content-type:text/html\r\n\r\n");
to = users;
amt = form.getvalue('deposit')
if(to!=0):
    try:
        con=cx_Oracle.connect('system/shyam@localhost')
        cur=con.cursor()
        sql='insert into Transfer(Transid,FROMACC,TOACC,AMOUNT) values(seq_person.nextval,:1,:2,:3)';
        print ("<h2>Hello sender %s </h2>" % users);
        print ("<h2>Hello to %s </h2>" % to);
        print ("<h2>Hello amt %s </h2>" % amt);
        cur.execute(sql,{'1':users,'2':to,'3':amt});
        

        sql2="update UserDetails set balance=balance+:1 where userid=:2";
        cur.execute(sql2,{'1':amt,'2':users});
        con.commit()
    except Exception as e:
                print("exception",e)


    finally:
            
            cur.close()
            con.close()