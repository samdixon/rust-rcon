import json
import time
import websocket

class CommandResultNotFound(BaseException):
    pass


class Command:
    def __init__(
        self,
        command: str,
        identifier: int,
        ws: websocket.WebSocket,
        name: str="WebRcon",
        retry_count: int=2
    ) -> None:
        self.command = command
        self.identifier = identifier
        self.name = name
        self.retry_count = retry_count
        self.ws = ws

    def _format_command(self):
        return json.dumps({
            "Identifier": self.identifier,
            "Message": self.command,
            "Name": self.name,
        })

    def run(self):
        retry_counter = 0
        self.ws.send(self._format_command())
        while True:
            res = json.loads(self.ws.recv())
            if retry_counter >= self.retry_count:
                raise CommandResultNotFound('command return not found')
            if res.get('Identifier') == self.identifier:
                break
            retry_counter += 1
        self.ws.close()
        return Response(
                res['Message'],
                res['Identifier'],
                res['Type'],
                res['Stacktrace']
            )


class Response:
    def __init__(self, Message: str, Identifier: int, Type: str, Stacktrace: str) -> None:
        self.Message = Message
        self.Identifier = Identifier
        self.Type = Type
        self.Stacktrace = Stacktrace

    def __repr__(self):
        return f"Response(Message: {self.Message}, Identifier: {self.Identifier}, Type: {self.Type}, Stacktrace: {self.Stacktrace})"

    def __str__(self):
        return f"Response(Message: {self.Message}, Identifier: {self.Identifier}, Type: {self.Type}, Stacktrace: {self.Stacktrace})"
