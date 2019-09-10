import json
from flask import Flask, request, abort

class TextAnalyzer:

    @staticmethod
    def analyze(text):

        result = {
            "textLength": {
                "withSpaces": 0,
                "withoutSpaces": 0
            },
            "wordCount": 0,
            "characterCount": {}
        }

        activeWord = False

        for c in text:

            result["textLength"]["withSpaces"] += 1

            if not c.isspace():
                result["textLength"]["withoutSpaces"] += 1
            else:
                activeWord = False

            if not c.isspace() and not activeWord:
                activeWord = True
                result["wordCount"] += 1

            if c.isalpha():
                if c in result["characterCount"]:
                    result["characterCount"][c] += 1
                else:
                    result["characterCount"][c] = 1
            
        return json.dumps(result, sort_keys=True, indent=4)


app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():

    try:
        data = request.json
        text = data["text"]

        return TextAnalyzer.analyze(text)

    except:
        abort(400)

if __name__ == "__main__":
    app.run()
            