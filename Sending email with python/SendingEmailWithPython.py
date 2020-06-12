import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Yeasin Arafath'
email['to'] = 'arafath.yeasin1019@gmail.com'
email['subject'] = 'You won 1,000,000 dollars'

email.set_content('I am a python master!!!')

with smtplib.SMTP(host='smtp.gmail.com', post=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('u1504038@student.cuet.ac.bd', 'arafath101990100307adib')
    smtp.send_message(email)
    print('All good boss')