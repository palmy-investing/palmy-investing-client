import requests


class Token:

    def __init__(self, api_token):
        self.token = api_token

    def format_token(self):
        return f"Token {self.token}"


class RequestHandler:

    def __init__(
            self,
            url: str,
            token: type(Token),
            handle=False,
            json_kwargs=None
    ):
        self.endpoint = url
        self.token = token
        self.handle = handle
        self.json_kwargs = json_kwargs if json_kwargs else {}

    def authorize(self):
        return {"Authorization": self.token.format_token()}

    def get(self):
        response = requests.get(
            headers=self.authorize(),
            url=self.endpoint
        )

        if self.handle:
            return self.handle_response(response)

        # Default process
        if response.status_code != 200:
            return {"error": "failed to fetch the data", "status": response.status_code}

        return response.json(**self.json_kwargs)

    @staticmethod
    def handle_response(response):
        """Overwrite this if self.handle = true"""
        pass


def palmy_get(handler=RequestHandler, **kwargs):
    request = handler(**kwargs)
    return request.get()

def x():
    pass