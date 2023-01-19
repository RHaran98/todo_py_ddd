class ToDoBaseException(Exception):
    message = "Generic inheritabke exception for todo domain"

    def __str__(self):
        return ToDoBaseException.message


class ToDoDescriptionValidationError(ToDoBaseException):
    message = "Improper description field for tasks"

    def __str__(self):
        return ToDoDescriptionValidationError.message


class BookIsbnAlreadyExistsError(Exception):
    message = "The book with the ISBN code you specified already exists."

    def __str__(self):
        return BookIsbnAlreadyExistsError.message