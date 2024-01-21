from app.containers import Container

"""
Super simple hello world function, get everything working with this first!
"""
def run():
    container = Container()
    json_msg_action = container.json_message_action

    return json_msg_action().run("Hello world")