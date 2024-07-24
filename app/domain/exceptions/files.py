from app.domain.exceptions.base import DomainException


class FileNotFoundException(DomainException):
    """File not found"""

    pass


class SaveFileWentWrongException(DomainException):
    """Save file went wrong"""

    pass
