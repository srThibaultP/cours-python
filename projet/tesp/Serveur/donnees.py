from pkgutil import get_data
from sqlite3 import Cursor
from webbrowser import get
from xml.etree.ElementTree import tostring 
import mysql.connector
from mysql.connector import errorcode
import requests
import cgi

# Connexion serveur bdd
form = cgi.FieldStorage()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="supervisionpython"
)

mycursor = mydb.cursor()
mydata = str.strip(form.getvalue("pc"))


requete = "SELECT `id`, `hostname`, `OS_NAME`, `uptime`, `kernel`, `CPUname`, `CPUfrequency`, `datetime`, `total`, `used`, `free`, `CPUmax` FROM `info_pc` WHERE `hostname`='"+mydata+"'"
mycursor.execute(requete)




# Page Web

print("Content-type: text/html; charset=utf-8\n")
myresult = mycursor.fetchall()

taille = len(myresult)-1
HDD = (myresult[taille][9]/myresult[taille][8])*100
cpu = (myresult[taille][6]/myresult[taille][11])*100

html = """<!DOCTYPE html>
<head>
    <title>Supervision</title>
    <meta charset="UTF-8">
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script type="text/javascript">
      google.charts.load('current', {'packages':['gauge']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['CPU', """
          
print(html)          
print (cpu)
print("""],
          ['HDD', """)
print(HDD)
print("""]
        ]);

        var options = {
          width: 400, height: 150,
          redFrom: 90, redTo: 100,
          yellowFrom:75, yellowTo: 90,
          minorTicks: 5
        };

        var chart = new google.visualization.Gauge(document.getElementById('chart_div'));

        chart.draw(data, options);

       
      }
    </script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Year', 'Frequence CPU'],
          """)

i=0
while i <= len(myresult)-1:
 print("['"+str(myresult[i][7])+"',")
 print(myresult[i][6])
 print("],") 
 i=i+1
        
html2="""
        ]);

        var options = {
          title: 'PC Performance',
          hAxis: {title: 'Year',  titleTextStyle: {color: '#333'}},
          vAxis: {minValue: 0}
        };

        var chart = new google.visualization.AreaChart(document.getElementById('graph'));
        chart.draw(data, options);
      }
    </script>
    
    
    
  </head>
  
  
  
  <body> 
  <div class="card bg-light mb-3">
  <div class="card-header">Donnees PC 4</div>
  <div class="card-body">
    <h5 class="card-title">Information Ressource</h5>
    <p class="card-text"></p>
    <center><div align="Center" id="chart_div" style="width: 400px; height: 120px;"></div><br><br></center>
    <center><div id="graph" style="width: 100%; height: 500px;"></div></center>
  </div>
  </div>
  <table class="table table-hover table-white">
  <thead>
    <tr>
      <th scope="col">Hostname</th>
      <th scope="col">OS</th>
      <th scope="col">Uptime</th>
      <th scope="col">CPU</th>
    </tr>
  </thead>
  <tbody>"""
print(html2) 

# i=0 
# while i < 2:
#   i=i+1
print('<tr><th scope="row">'+myresult[taille][1]+'</th><td>'+myresult[taille][2]+'</td><td>'+str(myresult[taille][3])+'</td><td>'+myresult[taille][5]+'</td></tr>')

html3= """
  </tbody>
</table>
"""

print(html3)

cursorMenus = mydb.cursor()

cursorMenus.execute("SELECT DISTINCT `hostname` FROM `info_pc`")
resultat = cursorMenus.fetchall()

print ('''<form action="donnees.py" method="POST"><center><div class="input-group mb-3">
  <div class="input-group-prepend"><button type="submit" value="pc"class="btn btn-primary">Rechercher</button></div>
      <select name="pc" class="custom-select" aria-label=".form-select-lg example" id="id_pc">
        <option selected>Selectionner le nom du pc</option>''')
i=0
while i <= len(resultat):
  
  print('''<option value="''')
  print(resultat[i][0])
  print('''">'''+resultat[i][0]+'''</option>''')
  i=i+1
  
print ('''</select></div></form></center>''') 


