from flask import Flask, render_template, request
import openai
import json
from dotenv import dotenv_values
import ast

app = Flask(__name__)


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
    prompt = f"""
        You are a color palette generating assistant who will generate 2 to 8 hexadecimal color code list.
        You will generate colors based on the descriptions and scenario that user provided, and answer colors in python list following below format:

        Q: 4 colors of Google brand
        A: [#4285F4', '#EA4335', '#FBBC05', '#34A853']

        Q: desert and sand in summer
        A: ['#8D5524', '#C68642', '#E0AC69', '#F1C27D', '#FFDBAC']

        Q: {user_input}
        A:
    """
    resp = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        max_tokens = 300
    )
    color_list = ast.literal_eval(resp["choices"][0]["text"].strip())
    return color_list


if __name__ == "__main__":
    app.debug = True
    app.run()
