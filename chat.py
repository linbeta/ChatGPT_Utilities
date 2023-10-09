# -*- coding: utf-8 -*-
import argparse
from dotenv import load_dotenv
import openai
import os

'''
有短期記憶力的terminal 版 chatGPT，主要使用gpt-4 model，並且結束後使用Markdown格式儲存對話紀錄與summary，可供下次對話繼續使用。
'''

initial_system_prompt = """
你是一個有記憶能力的AI助理，除了回答我的問題以外，還會另外彙整我們對話中的summary，供我未來參考。summary的部分請使用markdown格式。
你精通繁體中文、英文，我們的對話內容可以依據適合的情境混合使用中英文，如遇特殊的專有名詞，可以以繁體中文為主，用括號標註英文原文，例如這樣：多啦A夢(Doraemon)又稱作小叮噹。\n

回應內容請依照以下格式：

[對話]
回覆給我的內容

[Summary in Markdown]
全部對話內容的重點整理
"""


def dialog(user_prompt: str, system_msg, model_name="gpt-4"):
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": "我周末想去看電影，請幫我上網查最近上映的10部電影，並推薦其中3部"},
        {"role": "assistant", "content": """
         [對話]
         對不起，我沒有上網查詢資料的功能，讓我將您的需求記錄下來。我建議您考慮查詢電影院的播放時間表或者是使用如Fandango, Yahoo電影等專門提供電影訊息的網站。

         [Summary in Markdown]
            * 使用者希望本週末去看電影
            * 使用者欲知道最近上映的10部電影，并希望我推薦其中3部
            * 被告知我無法直接上網查詢，但建議他上電影院官網或電影訊息網站查詢
         """},
        {"role": "user", "content": f"{user_prompt}"},
    ]

    resp = openai.ChatCompletion.create(
        model = model_name,
        messages = messages,
    )

    # TODO: 計算使用的token，並可以累計

    # 單一則回覆的內容
    resp_text =  resp["choices"][0]["message"]["content"]
    token_usage =  resp["usage"]["total_tokens"]
    return resp_text, token_usage



def save_result_markdown(context, summary):
    pass

def main():
    # TODO: 寫可以持對對話的loop機制，累計tokens、並可以儲存最後的重點。
    total_usage = 0
    summary = ""
    assistant_answer = ""
    while True:
        system_prompt = initial_system_prompt + summary
        user_input = input("YOU: ")
        if user_input == "exit":
            break

        response, usage = dialog(user_input, system_prompt, "gpt-4")
        try:
            dialog_summary = response.split("[Summary in Markdown]")[1]
            assistant_answer = response.split("[對話]")[1].split("[Summary in Markdown]")[0]
        except Exception as e:
            print(e)
            print(f"chatGPT回覆的內容長這樣：\n{response}")
            dialog_summary = ""

        summary += dialog_summary
        total_usage += usage
        print(f"ASSISTANT: {assistant_answer}", "\n--------------\n")
        print(f"Summary: {dialog_summary}")
        print(f"Total usage: {total_usage}\n")



if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()
