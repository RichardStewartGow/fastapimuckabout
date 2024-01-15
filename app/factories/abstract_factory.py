from app.enums import concrete_factories

def get_factory(target: concrete_factories):
    return target()