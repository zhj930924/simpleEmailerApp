import smtplib

def send_emails(emails, schedule, forecast):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = input("What's your password?")
    from_email = 'zhj930924@gmail.com'
    server.login(from_email, password)

    # Send to entire email List
    for to_email, name in emails.items():
        message = 'Subject: Welcome to the CVille!\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        message += 'Hope to see you there!'
        server.sendmail(from_email, to_email, message)

    server.quit()
