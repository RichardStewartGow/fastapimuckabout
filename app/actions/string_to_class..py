import sys

def run(target_class: str):
    return getattr(sys.modules[__name__], target_class)