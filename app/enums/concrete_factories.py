from enum import Enum
from app.factories import response_strategy_factory

class ConcreteFactoryEnums(Enum):
    RESPONSE_STRATEGY_FACTORY = response_strategy_factory

    @staticmethod
    def from_string(input: str):
        if input.upper() == 'RESPONSE_STRATEGY_FACTORY':
            return concrete_factory_enums.RESPONSE_STRATEGY_FACTORY
        
        raise ValueError();