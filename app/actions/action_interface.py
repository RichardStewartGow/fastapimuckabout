class ActionInterface:
    def run(self, payload):
        """
        define common interface for actions, everything has a self reference and a duck typed payload
        """
