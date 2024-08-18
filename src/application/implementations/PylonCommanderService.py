from src.domain.abstractions.PylonCommander import PylonCommander


class PylonCommanderService(PylonCommander):
    """Exposes methods for inter-client communication."""
    def execute_command(self):
        pass
    def await_command(self):
        pass