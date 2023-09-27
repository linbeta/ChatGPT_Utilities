# -*- coding: utf-8 -*-
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT = """
你是一個精通於繁體中文的重點擷取助手，協助我將技術文件中的描述內容，濃縮彙整為口語化、重點式且有連貫性的行銷講稿。
我會提供長篇的功能說明文字，內容來自我的技術文件，請你幫我整理成可以搭配power point簡報及動畫分鏡描述解說的行銷推廣講稿。
我的power point規劃為20頁，每頁的講稿需要在55個繁體中文字以內，如有較長的內容描述可以拆分為2頁講稿。
輸出講稿的總字數需在800至1000字之間。

請你幫我Think step by step，用鋪陳、活潑的敘述協助聽眾想像並了解種個計劃的內容與價值。
整體的講稿口吻要專業、語意順暢且活潑，並適時的使用同義字詞，讓每一頁的內容皆能獨特而具意義。

最後，請將輸出的結果請一次呈現給我，輸出格式如下：

"""

filecontent = """
"""

def shorten_content(filecontent: str, model_name, filename: str):
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": f"內容: {filecontent}"},
    ]

    print("processing....")
    resp = openai.ChatCompletion.create(
        model = model_name,
        messages = messages,
        temperature = 0.8
    )
    output = resp["choices"][0]["message"]["content"]
    print(output)
    usage = resp["usage"]
    print(usage)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    shorten_content(filecontent, "gpt-4", "output-1.txt")
