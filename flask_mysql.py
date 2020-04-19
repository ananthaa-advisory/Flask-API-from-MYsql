from flask import Flask, render_template
import mysql.connector
# Source as which is altered accordingly: 
#https://www.reddit.com/r/flask/comments/evr3jk/display_mysql_table_with_html/

app = Flask(__name__, template_folder="/root/templates")

#@app.route('/')
#def index():
 #   return render_template("index.html")

#if __name__ == "__main__":
#    app.run(debug=True)

@app.route('/select', methods=['GET'])
def employee():
    dbconfig = { 'host': '127.0.01', 'user': 'root', 'password': 'root', 'database' :'testdb' }
    conn = mysql.connector.connect(**dbconfig)
    mycursor = conn.cursor()
   
    mycursor.execute("SELECT * FROM testtable")

    myresult = mycursor.fetchall()
    
    return render_template("selectindex.html", data=myresult)

#    for data in myresult:
 #       for i in data:
  #          print(i)




if __name__ == "__main__":
    app.run(debug=True)
