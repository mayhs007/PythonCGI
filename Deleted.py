#!C:\Users\Shyam\AppData\Local\Programs\Python\Python36\python.exe
import cgi, cgitb 
import cx_Oracle
form = cgi.FieldStorage() 
users = form.getvalue('user')
fname = form.getvalue('fname')
print ("Content-type:text/html\r\n\r\n");
try:
    con=cx_Oracle.connect('system/shyam@localhost')
    cur=con.cursor()
    sql='insert into DeletedAcc(Userid,Fname) values(:1,:2)';
    cur.execute(sql,{'1':users,'2':fname});
    print ("<h2>Hello sender %s </h2>" % users);
    print ("<h2>Hello sender %s </h2>" % fname);
    con.commit()
    sql2='delete from UserDetails where userid= :3';
    cur.execute(sql2,{'3' :users});
    con.commit()
    redirectURL="../Python/loginmain.html";
    print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />');
except Exception as e:
            print("exception",e)

finally:
        
        cur.close()
        con.close()