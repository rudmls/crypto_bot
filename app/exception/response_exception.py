class ResponseException(Exception):

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return str({
            'status_code': self.status_code,
            'message': self.message
        })
