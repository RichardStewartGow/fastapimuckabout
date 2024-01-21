"""
Hold stategys as enums and resolve from string
"""
from enum import Enum
from app.strategies.hello_world_strategy import run as hello_world_strategy
from app.strategies.reverse_strategy import run as reverse_strategy


class StrategyEnums(Enum):
    """
    When you want to add a new strategy add its run method and selecting logic
    """
    HELLO_WORLD_STRATEGY = hello_world_strategy
    REVERSE_STRATETGY = reverse_strategy

    @staticmethod
    def from_type_string(qtype: str, payload: str|None):
        """
        turn string into relevant strategy class, break out when it gets bigger than 4 cases
        """
        match qtype.upper():
            case "HELLO":
                return StrategyEnums.HELLO_WORLD_STRATEGY()
            case "REVERSE":
                return StrategyEnums.REVERSE_STRATETGY(payload)
            case _:
                raise ValueError('Unable to build a strategy')
