import json
from flask import Flask, request, abort, jsonify

class TextAnalyzer:

    @staticmethod
    def analyze(text):

        textLength = 0
        numSpaces = 0
        wordCount = 0
        characterCount = {}

        activeWord = False

        for c in text:

            textLength += 1

            if c.isspace():
                numSpaces += 1
                activeWord = False

            if not c.isspace() and not activeWord:
                activeWord = True
                wordCount += 1

            if c.isalpha():
                c_asLowerCase = c.lower()
                if c_asLowerCase in characterCount:
                    characterCount[c_asLowerCase] += 1
                else:
                    characterCount[c_asLowerCase] = 1

        return json.dumps(
            {
                "textLength":
                {
                    "withSpaces": textLength, 
                    "withoutSpaces": textLength-numSpaces
                }, 
                "wordCount": wordCount, 
                "characterCount": [ {k: characterCount[k]} for k in sorted(characterCount)]
            }
        )


app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    
    try:
        data = request.json
        text = data["text"]

        return jsonify(TextAnalyzer.analyze(text))

    except:
        abort(400)

if __name__ == "__main__":
    app.run()
            