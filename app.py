from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'
client = Client(account_sid, auth_token)

call = client.calls.create(twiml='''<Response>
  <Say>Hello Aditya</Say>
  <Play>http://pages.cs.wisc.edu/~gtracy/twilio/NeverGonnaGiveYouUp.mp3</Play>
</Response>''',
                        to='destination_number',
                        from_='your_purchased_twilio_number'
                    )

print(call.sid)
