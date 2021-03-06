class BeerNameAlreadyExistsException(Exception):
    status_code = 422
    error_code = "exception:beer_name_already_exists"

    def __init__(self, name: str):
        message = f"Beer name '{name}' already exists."
        self._message = message

        super(BeerNameAlreadyExistsException, self).__init__(message)

    @property
    def message(self):
        return self._message
