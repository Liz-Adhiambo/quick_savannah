from __future__ import print_function
from decouple import config

import africastalking
class SMS:
    def __init__(self):
		# Set your app credentials
        self.username = "sandbox"
        self.api_key = config('africas_api_key')

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self,number):
        # Set the numbers you want to send to in international format
        recipients = [number]

        # Set your message
        message = "Congratulations! You have successfully placed your order! "

        # Set your shortCode or senderId
        sender = config('sender')
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, recipients, sender)
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))

# if __name__ == '__main__':
#     SMS().send()