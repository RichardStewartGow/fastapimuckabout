from enum import Enum
from app.factories.response_strategy_factory import get_strategy as response_strategy_factory

class ConcreteFactoryEnums(Enum):
    RESPONSE_STRATEGY_FACTORY = response_strategy_factory

    @staticmethod
    def from_string(query: str, type: str):
        if query.upper() == 'RESPONSE':
            return ConcreteFactoryEnums.RESPONSE_STRATEGY_FACTORY(type)
        
        raise ValueError();