import requests
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def load_word_list(filename):
    with open(filename, "r") as file:
        words = file.read().splitlines()
    return words

def is_username_available(username):
    response = requests.get(f"https://www.instagram.com/{username}/")
    return "Sorry, this page isn't available" in response.text

def send_email(subject, body):
    email_address = "your_email@example.com"
    email_password = "your_email_password"
    smtp_server = "smtp.example.com"
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = "hairyharry@kakao.com"
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, "hairyharry@kakao.com", msg.as_string())
    server.quit()

while True:
    word_list = load_word_list("words_alpha.txt")
    available_usernames = []

    for word in word_list:
        if len(word) >= 3 and len(word) <= 30:  # Limit username length as per Instagram rules
            username = word
            if is_username_available(username):
                available_usernames.append(username)
                send_email("New Username Available", f"New available username: {username}")

    with open("available_usernames.txt", "a") as file:
        for username in available_usernames:
            file.write(username + "\n")

    print("Available usernames:")
    print(available_usernames)

    time.sleep(60)  # Wait for 1 minute before checking again
