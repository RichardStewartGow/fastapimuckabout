from app.containers import Container
from app.strategies.strategy_iterface import StrategyInterface

class IsValidStrategy(StrategyInterface):
    def __init__(self):
        container = Container()
        self.json_msg_action = container.json_message_action
        self.is_valid = container.is_valid

    def run(self, payload: dict):
        """
        Reverse the input payload into a new string 
        using slicing as strings are immutate iterateble objects then
        use action to return as a Json response

        payload (str): string to reverse
        """
        p = True
        q = False

        output = f"{p} => {q} is Valid" if self.is_valid(p,q) else "{p} => {q} is Not Valid"

        return self.json_msg_action(output)



