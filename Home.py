#!C:\Users\Shyam\AppData\Local\Programs\Python\Python36\python.exe
import cgi, cgitb 
import cx_Oracle

form = cgi.FieldStorage() 
user = form.getvalue('userid')
pwd  = form.getvalue('password')
print ("Content-type:text/html\r\n\r\n");
try:
        #if(x==0):
         #       print ("<h2>LOGIN INCORRECT</h2>");
       
        con=cx_Oracle.connect('system/shyam@localhost')
        cur=con.cursor()
        qu='select fname from UserDetails where userid= :1 and password= :2';
        cur.execute(qu,{'1':user,'2':pwd})
        con.commit()
        res = cur.fetchall()
        
        if(res!=[]):
                    sql2='delete from Fail where userid= :3';
                    cur.execute(sql2,{'3' :user});
                    con.commit()
                    fname=res[0];
                    print('<html>');
                    print(' <head>');
                    print('  </head>');
                    print('<link rel="stylesheet" href="button.css">');
                    print('<link rel="stylesheet" href="container.css">');
                    print(' <link rel="stylesheet" href="bootstrap.min.css">');
                    print(" <link href='https://fonts.googleapis.com/css?family=Cinzel Decorative' rel='stylesheet'>");
                    print('  <body>');
                    print('<div class="container">');
                    print('<div class="row">');
                    print('<div class="col-md-8 col-md-offset-2">');
                    print('<div class="panel panel-default">');
                    print(' <div class="panel-heading">REGISTER</div>');
                    print('<div class="panel-body">');
                    print(" <form method='post' action='Transfer.py?user="+user+"'>");
                    print('     <input type="number" min="1" name="aumt" required>');
                    print('      <label for="aumt">Amount To be sent</label>');
                    print('      <input type="text" name="To" required>');
                    print('      <label for="To">Transfer To</label>');
                    print('      <input type="submit" name="Trans" class="btn btn-primary" value="TRANSFER">');
                    print('  </form>');
                    print("<form method='post' action='Deleted.py?user="+user+"&fname=%s'>" %fname);
                    print('<input type="submit" name="Trans" class="btn btn-danger" value="DELETED_ACCOUNT">');
                    print("</form>");  
                    print(" <form method='post' action='Deposit.py?user="+user+"'>");
                    print('     <input type="number" min="1" name="deposit" required>');
                    print('      <label for="aumt">AMOUNT TO BE DEPOSIT</label>');
                    print('      <input type="submit" name="dep" class="btn btn-primary" value="TRANSFER_TO_ME">');
                    print("</form>");
                    print(" <form method='post' action='Withdraw.py?user="+user+"'>");
                    print('     <input type="number" min="1" name="withdraw" required>');
                    print('      <label for="withdraw">AMOUNT TO BE WITHDRAW</label>');
                    print('      <input type="submit" name="dep" class="btn btn-primary" value="GIVE_TO_ME">');
                    print("</form>");
                    
                    print('  </body>');
                    print('  </html>');
        else:
            qu1='select fname from AdminDetails where userid= :1 and password= :2';
            cur.execute(qu1,{'1':user,'2':pwd})
            con.commit()
            res1 = cur.fetchall()
            if(res1!=[]):
                print ("<h2>Hello admfsdin</h2>");
            else:
                
                sql='Insert into Fail(Userid) values(:1)'
                cur.execute(sql,{'1':user});
                con.commit();
                sql2='select count(userid) from Fail where userid=:1'
                cur.execute(sql2,{'1':user});
                con.commit();
                result=cur.fetchone();
                res3=result[0];
                if(res3>3):
                       
                       print("<script>");
                       print("alert('UR BLOCKED CONTACT ADMIN')");
                       print("</script>");  
                redirectURL="../Python/Loginmain.html";
                print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />');           
               
except Exception as e:
        print("exception",e)
        

finally:
        cur.close()
        con.close()



