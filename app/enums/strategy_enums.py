from enum import Enum
from app.strategies.hello_world_strategy import run as hello_world_strategy

class StrategyEnums(Enum):
    HELLO_WORLD_STRATEGY = hello_world_strategy

    @staticmethod
    def from_type_string(type: str):
        if type.upper() == 'HELLO':
            return StrategyEnums.HELLO_WORLD_STRATEGY()
        
        raise ValueError('Unable to build a strategy')