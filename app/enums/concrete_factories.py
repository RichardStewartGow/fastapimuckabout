from enum import Enum
from app.factories.response_strategy_factory import get_strategy as response_strategy_factory

class ConcreteFactoryEnums(Enum):
    """
    enums as the get strategy method from any concrete factory
    """
    RESPONSE_STRATEGY_FACTORY = response_strategy_factory

    @staticmethod
    def from_string(query: str, qtype: str, payload: str|None):
        """
        Make this accessible where ever we invoke the enum, 
        make factory class from string and pass down type arg
        """
        match query.upper():
            case "RESPONSE":
                return ConcreteFactoryEnums.RESPONSE_STRATEGY_FACTORY(qtype, payload)
            case _:
                raise ValueError('Unable to build a response strategy factory')
       