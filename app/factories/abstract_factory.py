from app.enums.concrete_factories import ConcreteFactoryEnums

##Use the inputted string/enums to create a class for more concrete constructors.
def get_factory(target: str):
    try:
        class_target = ConcreteFactoryEnums.from_string(target)
    except ValueError:
        raise ValueError(f"{target} is not a valid query")

    return class_target()