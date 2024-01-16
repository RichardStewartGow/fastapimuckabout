from app.enums.strategy_enums import StrategyEnums

def get_strategy(strategy_target: StrategyEnums):
    if (strategy_target == StrategyEnums.HELLO_WORLD_STRATEGY):
        return StrategyEnums.HELLO_WORLD_STRATEGY()
    
    raise ValueError()