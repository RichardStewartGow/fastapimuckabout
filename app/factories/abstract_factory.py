"""
abstract factory
"""
from app.enums.concrete_factories import ConcreteFactoryEnums

##Use the inputted string/enums to create a class for more concrete constructors or throw error if no match.
def get_factory(query: str, qtype: str, payload: str|None):
    """
    create concrete factory from string by enum
    """
    try:
        class_target = ConcreteFactoryEnums.from_string(query, qtype, payload)
    except ValueError as exc:
        raise ValueError(f"{query} is not a valid query") from exc

    return class_target
