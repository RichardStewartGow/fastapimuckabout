from app.actions.json_message_action import run as json_make

"""
Reverse the input payload into a new string using slicing as strings are immutate iterateble objects then
use action to return as a Json response

payload (str): string to reverse
"""
def run(payload: str):
    return json_make(payload[::-1])