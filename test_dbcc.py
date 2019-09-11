import pytest
import json
from dbcc import AnalyzedText

class TestExample:

    analyzedExampleText = AnalyzedText("hello 2 times  ")

    def test_wordCount(self):
        assert self.analyzedExampleText.wordCount() == 3

    def test_textLengthWithSpaces(self):
        assert self.analyzedExampleText.textLengthWithSpaces() == 15

    def test_textLengthWithoutSpaces(self):
        assert self.analyzedExampleText.textLengthWithoutSpaces() == 11

    def test_characterCount(self):
        assert self.analyzedExampleText.characterCount() == [
        {"e": 2},
        {"h": 1},
        {"i": 1},
        {"l": 2},
        {"m": 1},
        {"o": 1},
        {"s": 1},
        {"t": 1}
        ]