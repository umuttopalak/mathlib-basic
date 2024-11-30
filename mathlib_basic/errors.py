class DivideError(Exception):
    """Custom exception for division errors."""

    def __init__(self, message="Cannot divide by zero!"):
        self.message = message
        super().__init__(self.message)
