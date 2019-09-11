import json
from flask import Flask, request, abort, jsonify

class AnalyzedText:

    def __init__(self, text):
        self.__textLength = 0
        self.__numSpaces = 0
        self.__wordCount = 0
        self.__characterCount = []
        
        activeWord = False
        characterCountDictionary = {}

        for character in text:

            self.__textLength += 1

            if character.isspace():
                self.__numSpaces += 1
                activeWord = False

            if not character.isspace() and not activeWord:
                activeWord = True
                self.__wordCount += 1

            if character.isalpha():
                lowerCaseCharacter = character.lower()
                if lowerCaseCharacter in characterCountDictionary:
                    characterCountDictionary[lowerCaseCharacter] += 1
                else:
                    characterCountDictionary[lowerCaseCharacter] = 1

        self.__characterCount = [ {k: characterCountDictionary[k]} for k in sorted(characterCountDictionary)]

    def textLengthWithSpaces(self):
        return self.__textLength

    def textLengthWithoutSpaces(self):
        return self.__textLength - self.__numSpaces

    def wordCount(self):
        return self.__wordCount

    def characterCount(self):
        return self.__characterCount

    def jsonResponse(self):
        return jsonify(
            {
                "textLength":
                {
                    "withSpaces": self.__textLength, 
                    "withoutSpaces": self.__textLength - self.__numSpaces
                }, 
                "wordCount": self.__wordCount, 
                "characterCount": self.__characterCount
            }
        )


app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    
    try:
        jsonData = request.json
        text = jsonData["text"]

        return AnalyzedText(text).jsonResponse()

    except:
        abort(400)

if __name__ == "__main__":
    app.run()
            