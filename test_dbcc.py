import pytest
import json
from dbcc import TextAnalyzer

class TestExample:

    exampleText = "hello 2 times  "

    def test_wordCount(self):
        response = json.loads(TextAnalyzer.analyze(self.exampleText))
        assert response["wordCount"] == 3

    def test_textLength(self):
        response = json.loads(TextAnalyzer.analyze(self.exampleText))
        assert response["textLength"]["withSpaces"] == 15
        assert response["textLength"]["withoutSpaces"] == 11

    def test_characterCount(self):
        response = json.loads(TextAnalyzer.analyze(self.exampleText))
        assert response["characterCount"] == {
        "e": 2,
        "h": 1,
        "i": 1,
        "l": 2,
        "m": 1,
        "o": 1,
        "s": 1,
        "t": 1
    }