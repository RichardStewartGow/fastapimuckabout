from app.actions.action_interface import ActionInterface

class IsValid(ActionInterface):
    def run(self, payload: dict) -> bool:
        return not(payload["p"]) or payload["q"]