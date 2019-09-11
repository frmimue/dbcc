import pytest
import json

from dbcc import app

class TestFlaskExample:

    app.testing = True
    client = app.test_client()

    exampleJson = {"text":"hello 2 times  "}

    def test_flaskBase(self):
        assert self.client.post('/analyze', json=self.exampleJson).status_code == 200


    def test_flaskWordCount(self):
        response = json.loads(self.client.post('/analyze', json=self.exampleJson).json)
        assert response["wordCount"] == 3

    def test_flaskTextLength(self):
        response = json.loads(self.client.post('/analyze', json=self.exampleJson).json)
        assert response["textLength"]["withSpaces"] == 15
        assert response["textLength"]["withoutSpaces"] == 11

    def test_flaskCharacterCount(self):
        response = json.loads(self.client.post('/analyze', json=self.exampleJson).json)

        assert response["characterCount"] == [
        {"e": 2},
        {"h": 1},
        {"i": 1},
        {"l": 2},
        {"m": 1},
        {"o": 1},
        {"s": 1},
        {"t": 1}
        ]


