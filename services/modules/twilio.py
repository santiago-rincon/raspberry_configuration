from twilio.rest import Client

account_sid = 'ACb256e72c88cb571ec127f0228b88d493'
auth_token = 'b3d6755e7ff3b9d09fec2faf96e4010e'
client = Client(account_sid, auth_token)

def send_message(body):
    registered_numbers  = client.outgoing_caller_ids.list()
    for number in registered_numbers:
        message = client.messages.create(
        from_ = '+16815885161',
        body = body,
        to = number.phone_number
        )