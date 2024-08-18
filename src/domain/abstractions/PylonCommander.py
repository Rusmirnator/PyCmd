from abc import abstractmethod
from src.domain.models import CommandRequest, CommandResult


class PylonCommander:
    """Provides protocol for application main use cases"""
    @abstractmethod
    def execute_command(self) -> CommandResult:
        """Executes given command and waits for its result."""

    @abstractmethod
    def await_command(self) -> CommandRequest:
        """Subscribes for remote commands using provided topic."""
