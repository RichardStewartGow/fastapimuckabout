from enum import Enum
from app.strategies.hello_world_strategy import run as hello_world_strategy
from app.strategies.reverse_strategy import run as reverse_strategy

class StrategyEnums(Enum):
    HELLO_WORLD_STRATEGY = hello_world_strategy
    REVERSE_STRATETGY = reverse_strategy

    @staticmethod
    def from_type_string(type: str, payload: str|None):
        match type.upper():
            case "HELLO":
                return StrategyEnums.HELLO_WORLD_STRATEGY()
            case "REVERSE":
                return StrategyEnums.REVERSE_STRATETGY(payload)
            case _:
              raise ValueError('Unable to build a strategy')
        
      