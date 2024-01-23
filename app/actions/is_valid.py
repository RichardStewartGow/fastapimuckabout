from app.actions.action_interface import ActionInterface

class IsValid(ActionInterface):
    def run(self, payload: dict) -> bool:
        return 'test'
        #return not(p) or q