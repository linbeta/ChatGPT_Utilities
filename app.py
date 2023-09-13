from flask import Flask, render_template, request
import openai
import json
from dotenv import dotenv_values
import ast

app = Flask(__name__,
    static_url_path="",
    static_folder="static",
)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    # app.logger.info("Prompting to palette")
    # app.logger.info(request.form.get("query"))
    config = dotenv_values(".env")
    openai.api_key = config["OPENAI_API_KEY"]
    # prompt engineering part
    user_input = request.form.get("query")

    resp = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a color palette generating assistant who will generate 2 to 8 hexadecimal color code list. You will generate colors based on the descriptions and scenario that user provided, and answer colors in python list following below format:"},
            {"role": "user", "content": "4 colors of Google brand"},
            {"role": "assistant", "content": "[#4285F4', '#EA4335', '#FBBC05', '#34A853']"},
            {"role": "user", "content": "desert and sand in summer"},
            {"role": "assistant", "content": "['#8D5524', '#C68642', '#E0AC69', '#F1C27D', '#FFDBAC']"},
            {"role": "user", "content": user_input},

        ],
        max_tokens = 300
    )
    color_list = ast.literal_eval(resp["choices"][0]["message"]["content"].strip())
    return color_list


if __name__ == "__main__":
    app.debug = False
    app.run(host="0.0.0.0", port=8000)
