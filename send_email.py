import smtplib,ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "stilianpavlov2@gmail.com"
    password = "tehgfkqnewpmgplo"
    receiver = "stilianpavlov2@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


