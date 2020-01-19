import json
import time

class Command:
    def __init__(self, command, identifier, ws, name="WebRcon"):
        self.command = command
        self.identifier = identifier
        self.name = name
        self.Message = Message(self.identifier, self.command)

        self.json_message = self.Message.json()
        self.ws = ws
        self.result = None
        self.parsed_result = None

    def run(self):
        self.ws.send(self.json_message)
        time.sleep(1)
        result = self.ws.recv()
        self.result = result
        self._parse_result()
        response = Response(
                self.parsed_result['Message'], 
                self.parsed_result['Identifier'],
                self.parsed_result['Type'],
                self.parsed_result['Stacktrace'])
        return response

    def _parse_result(self):
        self.parsed_result = json.loads(self.result)

class Message:
    def __init__(self, Identifier, Message, Name="WebRcon"):
        self.Identifier = Identifier
        self.Message = Message
        self.Name = Name

    def json(self):
        return json.dumps({
                "Identifier": self.Identifier,
                "Message": self.Message,
                "Name": self.Name
                })

class Response:
    def __init__(self, Message, Identifier, Type, Stacktrace):
        self.Message = Message
        self.Identifier = Identifier
        self.Type = Type
        self.Stacktrace = Stacktrace

    def __str__(self):
        return f"{self.Message}, {self.Identifier}, {self.Type}, {self.Stacktrace}"
