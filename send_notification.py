from twilio.rest import Client
import datetime
import random

account_sid = 'your id '
account_auth_token = 'token'

from_whatsapp = 'whatsapp:your twilio'
to_my_number = 'whatsapp:your own'

challenges = [
        "your defined custom message"
]

def daily_send():
    msg = random.choice(challenges)
    client = Client(account_sid, account_auth_token)
    message = client.messages.create(
        body=f"Yourcustom message {datetime.date.today()}:\n\n{msg}",
        from_=from_whatsapp,
        to=to_my_number
    )
    print(f"Message sent: {message.sid}")

if __name__ == "__main__":
    daily_send()
