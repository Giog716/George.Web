from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    nume = request.form['nume']
    email = request.form['email']
    mesaj = request.form['mesaj']

    # Configurarea email-ului
    to = 'your-email@gmail.com'  # Înlocuiește cu adresa ta Gmail
    subject = f'Mesaj de la {nume}'
    body = f'Nume: {nume}\nEmail: {email}\nMesaj:\n{mesaj}'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to

    # Trimiterea email-ului prin Gmail
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('terestro3@gmail.com', 'your-email-password-or-app-password')  # Înlocuiește cu adresa ta și App Password-ul
            server.send_message(msg)
        return redirect(url_for('index'))
    except Exception as e:
        print(f'Eroare la trimiterea mesajului: {e}')
        return 'Eroare la trimiterea mesajului. Te rugăm să încerci din nou.', 500

if __name__ == '__main__':
    app.run(debug=True)
