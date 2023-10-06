from twilio.rest import Client

account_sid = 'ACb256e72c88cb571ec127f0228b88d493'
auth_token = '8733747f560fc21c6bfcdd0cfa29ec25'
client = Client(account_sid, auth_token)

def send_message(body):
    registered_numbers  = client.outgoing_caller_ids.list()
    for number in registered_numbers:
        message = client.messages.create(
        from_ = '+16815885161',
        body = body,
        to = number.phone_number
        )