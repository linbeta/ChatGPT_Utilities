import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT = """
You will recieve a file's contents as text.
Generate a code review for the file. Indicate what changes should be made to improve its style, performance, readability and manintainability.
If there are any reputable libraries that could be introduced to improve the code, please suggest them.
Be kind and constructive.
For each suggested change, include line numbers to which your are referring.
"""

filecontent = """
def a_function(x, y):
    return x ** y + x * y
"""

def code_review(file_path, model_name="gpt-3.5-turbo"):
    with open(file_path, 'r') as f:
        content = f.read()
    reviews = make_code_review_request(content, model_name)
    print(reviews)


def make_code_review_request(filecontent: str, model_name):
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": f"Code review the following file: {filecontent}"},
    ]

    resp = openai.ChatCompletion.create(
        model = model_name,
        messages = messages,
    )

    return resp["choices"][0]["message"]["content"]


if __name__ == "__main__":
    code_review("app.py", "gpt-4")
