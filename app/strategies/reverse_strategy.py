from app.containers import Container


def run(payload: str):
    """
    Reverse the input payload into a new string using slicing as strings are immutate iterateble objects then
    use action to return as a Json response

    payload (str): string to reverse
    """
    container = Container()
    json_msg_action = container.json_message_action

    return json_msg_action().run(payload[::-1])
