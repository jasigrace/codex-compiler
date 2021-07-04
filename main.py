import requests
from flask import Flask, render_template, request

app = Flask(__name__)

CODEX_URL = "https://codexweb.netlify.app/.netlify/functions/enforceCode"


@app.route('/', methods=["POST", "GET"])
def home():
    file = []
    languages = ["C", "C++", "Java", "Python"]
    language_values = ['c', 'cpp', 'java', 'py']
    if request.method == "POST":
        code = request.form.get('editor')
        language = request.form.get('languages')
        user_input = request.form.get('input')
        parameters = {
            "code": code,
            "language": language,
            "input": user_input
        }
        file.append(code)
        file.append(language)
        file.append(user_input)

        response = requests.get(url=CODEX_URL, json=parameters)
        if request.form.get('submit'):
            print("HI")
            with open('test.txt', 'w') as code_file:
                code_file.write(f'Code:\n{file[0]}\n\nInput:\n{file[2]}\n\nOutput:\n {response.json()["output"]}')
        return render_template('index.html', code=code, output=response.json()['output'], user_input=user_input, selected_lang=languages[language_values.index(language)], languages=languages, language_values=language_values)
    return render_template('index.html', languages=languages, language_values=language_values)

# public class program{public static void main(String [] args){System.out.println(5+5+6);}}


if __name__ == '__main__':
    app.run(debug=True)
