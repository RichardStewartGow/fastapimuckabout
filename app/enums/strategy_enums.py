from enum import Enum
from app.strategies.hello_world_strategy import run as hello_world_strategy

class StrategyEnums(Enum):
    HELLO_WORLD_STRATEGY = hello_world_strategy
