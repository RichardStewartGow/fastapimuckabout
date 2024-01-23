"""
common interface for strategies
"""
class StrategyInterface:
    """
    Likewise Very empty, we only want to semi enforce one method
    """
    def run(self, payload):
        """
        all accesses via run everything has a self 
        reference and a duck typed payload to allow maxium flexibility
        """
