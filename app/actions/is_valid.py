from app.actions.action_interface import ActionInterface

class IsValid(ActionInterface):
    def run(self, p: bool, q: bool) -> bool:
        return not(p) or q