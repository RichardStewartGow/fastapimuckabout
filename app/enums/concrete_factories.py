from enum import Enum
from app.factories.response_strategy_factory import get_strategy as response_strategy_factory

class ConcreteFactoryEnums(Enum):
    RESPONSE_STRATEGY_FACTORY = response_strategy_factory

    ##Make this accessible where ever we invoke the enum, make factory class from string and pass down type arg
    @staticmethod
    def from_string(query: str, type: str, payload: str|None):
        match query.upper():
            case "RESPONSE":
                return ConcreteFactoryEnums.RESPONSE_STRATEGY_FACTORY(type, payload)
            case _:
                raise ValueError('Unable to build a response strategy factory')
       