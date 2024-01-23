from app.containers import Container
from app.strategies.strategy_iterface import StrategyInterface

class HelloWorldStrategy(StrategyInterface):
    def __init__(self):
        container = Container()
        self.json_msg_action = container.json_message_action


    def run(self):
        """
        Super simple hello world function, get everything working with this first!
        """

        return self.json_msg_action().run("Hello world")
