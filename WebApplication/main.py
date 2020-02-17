from flask import Flask, request, render_template, redirect
import random
import mysql.connector

SELECT_SHORT_LINK = "SELECT Short_Url FROM URLS WHERE Long_Url = %s"
SELECT_LONG_LINK = "SELECT Long_Url FROM URLS WHERE Short_Url = %s"
processed_text = ""
route = "localhost:5000"
link_range = 9
char_array = ['a','b','c','d','e','f','g','h','i','l','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','L','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

app = Flask(__name__)
config = {
  'user': 'X2N5VVsN16',
  'password': 'iyCCXOqcSF',
  'host': 'remotemysql.com',
  'database': 'X2N5VVsN16',
  'raise_on_warnings': True
}
def remove_symbols(word):
    for x in word:
        word = word.replace("'","")
        word = word.replace(")","")
        word = word.replace("(","")
        word = word.replace(",","")
    return word

@app.route("/<route_id>")
def redirection(route_id):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    route_id = "/"+route_id
    cursor.execute(SELECT_LONG_LINK,(route_id,))
    redirect_link = str(cursor.fetchone())
    cursor.close()
    cnx.close()
    redirect_link = remove_symbols(redirect_link)
    return redirect("http://"+redirect_link, code=302)
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def my_form_post():
    newer_link = "/"
    #connect to db
    user_link = request.form['text']
    processed_link = user_link.lower()
    if (len(user_link)>255):
        return render_template("home.html", processed_link = "link is too long (max length = 255)")
    else:
        for x in range(link_range):
            newer_link = newer_link+random.choice(char_array)
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(buffered=True)
        cursor.execute(SELECT_SHORT_LINK,(processed_link, ))
        short_link = cursor.fetchone()
        if  short_link == None :
            cursor.execute("INSERT INTO URLS(Long_Url, Short_Url) VALUES (%s, %s)", (processed_link, newer_link))
            cnx.commit()
        else:
            cursor.execute("SELECT Short_Url FROM URLS WHERE Long_Url = %s", (processed_link, ) )
            newer_link = str(cursor.fetchone())
            newer_link = remove_symbols(newer_link)
        cursor.close()
        cnx.close()
        return render_template("home.html", processed_link = route + newer_link)

if __name__ == "__main__":
    app.run(debug=True)
