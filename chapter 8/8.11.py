def send_messages(messages, sent_messages):
    while messages:
        sent_message = messages.pop()
        print("message incoming")
        sent_messages.append(sent_message)
       

def show_messages(messages):
    for message in messages:
        print(f"you recive a message that says: {message}")

sent_messages = []
messages = ['hello', 'bye bye', 'aloha', 'konichiwa'] 

print(messages)

send_messages(messages[:], sent_messages)
show_messages(sent_messages)

print(sent_messages)
print(messages)
