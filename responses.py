

def handle_response(message) -> str:
    message_processed = message.lower()

    if message_processed == "hello":
        return "Hello! I am a machine."

    if message_processed == "bagon":
        return "da goat"
