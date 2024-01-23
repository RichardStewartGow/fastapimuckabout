"""
Hold stategys as enums and resolve from string
"""
from enum import Enum
from app.strategies.hello_world_strategy import HelloWorldStrategy
from app.strategies.reverse_strategy import ReserveStrategy
from app.strategies.is_valid_strategy import IsValidStrategy


class StrategyEnums(Enum):
    """
    When you want to add a new strategy add its run method and selecting logic
    """
    HELLO_WORLD_STRATEGY = HelloWorldStrategy
    REVERSE_STRATETGY = ReserveStrategy
    IS_VALID_STRATEGY = IsValidStrategy

    @staticmethod
    def from_type_string(qtype: str, payload: str|dict|None):
        """
        turn string into relevant strategy class, break out when it gets bigger than 4 cases
        """
        match qtype.upper():
            case "HELLO":
                test = StrategyEnums.HELLO_WORLD_STRATEGY.value
                return test
            case "REVERSE":
                return StrategyEnums.REVERSE_STRATETGY.value
            case "VALID":
                return StrategyEnums.IS_VALID_STRATEGY.value
            case _:
                raise ValueError('Unable to build a strategy')
