from app.enums.concrete_factories import ConcreteFactoryEnums

def get_factory(target: str):

    try:
        class_target = ConcreteFactoryEnums.from_string(target)
    except ValueError:
        raise ValueError(f"{target} is not a valid query")
    
    print(class_target)
    return class_target()