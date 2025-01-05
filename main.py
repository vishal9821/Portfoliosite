from flask import Flask, render_template,request
from datetime import date
import smtplib
import os
EMAIL = os.getenv('email')
PASSWORD = os.getenv('pass')
RECEIVER = os.getenv('rec')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/home-2")
def homepage2():
    return render_template("home2.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        m_type = request.form.get("messagetype")
        message = request.form.get("message")
        date_today = date.today()
        mail_body = f"subject:Message from portfolio site user {name}\n\nName={name}\nEmail={email}\nMessage Type={m_type}\nMessage={message}\nDate={date_today}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=RECEIVER,msg=mail_body)
        message = f"{name} Your message has been sent successfully !"
        return render_template("contact.html",messages=message)
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=False)