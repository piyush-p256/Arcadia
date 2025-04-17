def generate_caption(event):
    return f"{event['event'].capitalize()} at {event['timestamp']}!"
