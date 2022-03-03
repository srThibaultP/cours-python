# import cgi
from xml.etree.ElementTree import tostring 
import mysql.connector
from mysql.connector import errorcode
import requests


# Connexion serveur bdd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="supervisionpython"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT `hostname` FROM `info_pc`")


# Page Web


# form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
print('''<head> <title>Supervision</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head>
    <body><center><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhowDnzY3YlnuojlQo65UUjBNt4MB6E-D8pQ&usqp=CAU"/><div class="mb-3"><center><a size="14" class="text-decoration-none">Selectionner le poste souhaiter</a></center>''')



print ('''<form action="donnees.py" method="GET"><center><div class="input-group mb-3">
  <div class="input-group-prepend"><button type="submit" value="pc" class="btn btn-primary">Rechercher</button></div>
      <select name="pc" class="custom-select" aria-label=".form-select-lg example" id="id_pc">
        <option selected>Selectionner le nom du pc</option>''')

myresult = mycursor.fetchall()
i=0
while i <= len(myresult)+1:
  
  print('''<option value="''')
  print(myresult[i][0])
  print('''">'''+myresult[i][0]+'''</option>''')
  i=i+1
  
print ('''</select></form></div></center>''') 

ending = "</body></html>"


print(ending)
# data = {"a_key": "a_value"}
# url = "donnees.py"
# response = requests.post(url, data)