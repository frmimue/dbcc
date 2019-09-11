import json
from flask import Flask, request, abort, jsonify

class AnalyzedText:

    def __init__(self, text):
        self.__textLength = 0
        self.__numSpaces = 0
        self.__wordCount = 0
        self.__characterCount = []

        self.__analyze(text)

    def __analyze(self, text):

        activeWord = False
        characterCountDictionary = {}

        # Analyze each character in the text individually

        for character in text:

            # Increase the text length by one for every character in the text

            self.__textLength += 1

            # If the current character is a space we increase the space counter by one, this also means that we are not processing a word anymore

            if character.isspace():
                self.__numSpaces += 1
                activeWord = False

            # If the current character is not a space and we are not already processing a word we have hit a new word, increasing the word counter by one and starting to process a new word

            if not character.isspace() and not activeWord:
                activeWord = True
                self.__wordCount += 1

            # If the current character is in the english alphabet we take the lower case version and increase the counter for it by one or set the counter to one if this is the first occurrence

            if character.isalpha():
                lowerCaseCharacter = character.lower()
                if lowerCaseCharacter in characterCountDictionary:
                    characterCountDictionary[lowerCaseCharacter] += 1
                else:
                    characterCountDictionary[lowerCaseCharacter] = 1

        # Turn the character counter into the final format 

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
            