#!C:\Users\Shyam\AppData\Local\Programs\Python\Python36\python.exe
import cgi,cgitb
print ("Content-type:text/html\r\n\r\n");
print ('<html>');
print ('<head>');
print('<link rel="stylesheet" href="button.css">');
print('<link rel="stylesheet" href="container.css">');
print('<link rel="stylesheet" href="bootstrap.min.css">');
print("<link href='https://fonts.googleapis.com/css?family=Cinzel Decorative' rel='stylesheet'>");
print ('</head>');
print('<style>');
print("body{");
print("font-family: 'Cinzel Decorative'");
print("}");
print("button{");
print("font-family:'Cinzel Decorative'");
print("}");
print('</style>');
print ('<body>');
#print ('<h2>Hello Word! This is my first CGI program</h2>');
print ('<div class="card">');
print('  <div class="container">');
print('	<h1> LOGIN</h1>');
print('	<form action="CGI.py" method="POST">');
print('	<div class="input-container">');
print('	<input type="text" id="userid" name="userid" required/>');
print('<label for="user">UserId</label>');
print('<div class="bar"></div>');
print('</div>');
print('<div class="input-container">     ');        
print('<input type="password" id="password" name="pass" required/>');
print('<label for="pass">Password</label>');
print('<div class="bar"></div>');
print('</div>');
print('<div class="tab">');
print("&nbsp<input type='submit' name='submit' class='btn btn-primary' value='Login'");
print('</div>');
print('</form>');
print ('</body>');
print ('</html>');

form=cgi.FieldStorage()
userid=form.getvalue('userid')
password=form.getvalue('password')
#print('<h1>%s</h1>' %userid);
print('<h1>%s</h1>' %password);
        	