from app.enums.strategy_enums import StrategyEnums

##Use the inputted string to make a concrete strategy or throw error if it dosent match
def get_strategy(type: str, payload: str|None):
    try:
        response = StrategyEnums.from_type_string(type, payload)
    except ValueError:
        raise ValueError(f"{type} is not a valid type")

    return response