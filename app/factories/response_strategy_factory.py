"""
strategy factory for anything require a response to the requesting user
"""
from app.enums.strategy_enums import StrategyEnums

##Use the inputted string to make a concrete strategy or throw error if it dosent match
def get_strategy(qtype: str, payload: str|None):
    """
    resolve strategy from string
    """
    try:
        response_class = StrategyEnums.from_type_string(qtype, payload)
    except ValueError as exc:
        raise ValueError(f"{qtype} is not a valid type") from exc

    return response_class
