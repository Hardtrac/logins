from flask import Flask, render_template, request, redirect, url_for, flash
import webbrowser
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate a secure random key

# Sample data for users and their Google Drive links
users = {
    'vinod': {'password': '1234', 'link': 'https://docs.google.com/spreadsheets/d/1UYQQilejDaiTGhECV9FrDsL-Y1hsybluxvxPeou52B8/edit#gid=105666129'},
    'realme': {'password': '1234', 'link': 'https://docs.google.com/spreadsheets/d/1UYQQilejDaiTGhECV9FrDsL-Y1hsybluxvxPeou52B8/edit#gid=105666129'},
    'brand3': {'password': 'pass3', 'link': 'https://drive.google.com/drive/folders/ghi789'},
    'brand4': {'password': 'pass4', 'link': 'https://drive.google.com/drive/folders/jkl012'},
    'brand5': {'password': 'pass5', 'link': 'https://drive.google.com/drive/folders/mno345'}
}

@app.route('/')
def index():
    return render_template('logins.html')

@app.route('/login', methods=['POST'])
def login():
    brand = request.form.get('brand')
    password = request.form.get('password')

    if brand in users and users[brand]['password'] == password:
        link = users[brand]['link']
        webbrowser.open(link)
        flash('Login successful!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Invalid brand name or password!', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
