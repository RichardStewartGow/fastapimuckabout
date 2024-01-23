from app.containers import Container
from app.strategies.strategy_iterface import StrategyInterface

class ReserveStrategy(StrategyInterface):

    def __init__(self):
        container = Container()
        self.json_msg_action = container.json_message_action

    def run(self, payload: str):
        """
        Reverse the input payload into a new string 
        using slicing as strings are immutate iterateble objects then
        use action to return as a Json response

        payload (str): string to reverse
        """
        return self.json_msg_action().run(payload[::-1])
