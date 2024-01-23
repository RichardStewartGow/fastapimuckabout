"""
abstract factory
"""
from app.enums.concrete_factories import ConcreteFactoryEnums


def get_factory(query: str, qtype: str, payload: str|dict|None):
    """
    create concrete factory from string by enum error if no match
    """
    try:
        class_target = ConcreteFactoryEnums.from_string(query, qtype, payload)
    except ValueError as exc:
        raise ValueError(f"{query} is not a valid query") from exc

    return class_target
