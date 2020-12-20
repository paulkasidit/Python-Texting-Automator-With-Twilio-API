import random, schedule, time

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

GOOD_MORNING_QUOTES = [
    "Good Morning Love! Hope you Have An Amazing Day <3",
    "Good Morning Sleepyhead.",
    "Get yo ass up",
    "Love you. Good morning"
]

GOOD_EVENING_QUOTES = [
    "Good Evening Love",
    "Sleep tight my love",
    "Have a good night my dear",
    "Good night. Love you"
]

def send_message(quotes_list=GOOD_MORNING_QUOTES):

    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )

#send message in the morning
schedule.every().day.at("10:58").do(send_message, GOOD_MORNING_QUOTES)

#send message in the evening
schedule.every().day.at("10:58").do(send_message, GOOD_EVENING_QUOTES)

#testing
schedule.every().day.at("15:47").do(send_message, GOOD_EVENING_QUOTES)

while True:
    #check whether a scheduled task
    #is pending or not
    schedule.run_pending()
    time.sleep(2)

