import weather
import mailer

def get_emails():
    # Reading emails from a file
    emails = {}

    try:
        email_file = open('emails2.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print(err)

    return emails

def get_schedule():
    # Reading schedule from a file
    try:
        schedule_file = open('schedule.txt', 'r')

        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedule

def main():
    emails = get_emails()
    ##print(emails)

    schedule = get_schedule()
    ##print(schedule)

    forecast = weather.get_weather_forecast()
    ##print(forecast)

    mailer.send_emails(emails, schedule, forecast)

main()

# api.openweathermap.org/data/2.5/weather?zip=22903,us

# 8c41d93a7030fd24a89875083f02344c
