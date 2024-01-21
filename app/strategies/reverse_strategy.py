from app.actions.json_message_action import JsonMessageAction

"""
Reverse the input payload into a new string using slicing as strings are immutate iterateble objects then
use action to return as a Json response

payload (str): string to reverse
"""
def run(payload: str):
    return JsonMessageAction().run(payload[::-1])