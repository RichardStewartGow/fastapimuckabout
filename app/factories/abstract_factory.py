from app.enums.concrete_factories import ConcreteFactoryEnums

##Use the inputted string/enums to create a class for more concrete constructors or throw error if no match.
def get_factory(query: str, type: str, payload: str|None):
    try:
        class_target = ConcreteFactoryEnums.from_string(query, type, payload)
    except ValueError:
        raise ValueError(f"{query} is not a valid query")

    return class_target