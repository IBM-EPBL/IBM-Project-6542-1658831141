import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("910019106033@student.autmdu.in")
to_email = To("910019106033@student.autmdu.in")
subject = "Sending with SendGrid"
content = Content("text/plain", "SendGrid Integrated With Python Successfully!")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)


