#!C:\Users\Shyam\AppData\Local\Programs\Python\Python36\python.exe
import cgi, cgitb 
import cx_Oracle
form = cgi.FieldStorage() 

print ("Content-type:text/html\r\n\r\n");

user = form.getvalue('userid');
pwd = form.getvalue('password');
fname = form.getvalue('fname');
lname = form.getvalue('lname');
type = form.getvalue('type')
bal = form.getvalue('amount');
l1 = form.getvalue('line1');
l2 = form.getvalue('line2');
city = form.getvalue('city');
state = form.getvalue('state');
pin = form.getvalue('pin');

x=int(bal);
try:
    if(type=="current" and x >= 5000):
        print("<h1>HELLO %s" % bal)
        con=cx_Oracle.connect('system/shyam@localhost')
        cur=con.cursor()
        sql='insert into UserDetails(Userid,Password,Fname,lname,balance,Type,Accno) values(seq_person.nextval,:2,:3,:4,:5,:6,seq_person.nextval)';
        cur.execute(sql,{'2':pwd,'3':fname,'4':lname,'5':bal,'6':type});
        sql2='insert into UserAddress(Userid,line1,line2,city,state,pincode) values(seq_person.nextval-1,:2,:3,:4,:5,:6)';
        cur.execute(sql2,{'2':l1,'3':l2,'4':city,'5':state,'6':pin});
        con.commit()
    elif(type=="savings"):
        print("<h1>HELLO %s" % bal)
        con=cx_Oracle.connect('system/shyam@localhost')
        cur=con.cursor()
        sql='insert into UserDetails(Userid,Password,Fname,lname,balance,Type,Accno) values(seq_person.nextval,:2,:3,:4,:5,:6,seq_person.nextval)';
        cur.execute(sql,{'2':pwd,'3':fname,'4':lname,'5':bal,'6':type});
        sql2='insert into UserAddress(Userid,line1,line2,city,state,pincode) values(seq_person.nextval-1,:2,:3,:4,:5,:6)';
        cur.execute(sql2,{'2':l1,'3':l2,'4':city,'5':state,'6':pin});
        con.commit()
    else:
       print("<script>");
       print("alert('BALANCE SHOULD BE ABOVE 5000')");
       print("</script>");
       redirectURL="../Python/Register.html";
       print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />');


except Exception as e:
            print("exception",e)


finally:
        
        cur.close()
        con.close()