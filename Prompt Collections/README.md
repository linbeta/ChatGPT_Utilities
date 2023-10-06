# 各種實用的PROMPT收集

平常在不同來源看到別人分享的實用prompt設定，包含 Chain-of-Thought 和 Chain-of-Density 等概念，需要有個筆記本把這些實用資訓整理起來，也方便之後和其他有興趣的人們分享討論。

## 翻譯類

加入chain of density的概念讓chatGPT的翻譯更接近人類翻譯，少一點機器翻譯感：
```HTML
<Prompt>
你是一位精通台灣繁體中文的專業翻譯，曾參與《紐約時報》和《經濟學人》繁體中文版的翻譯工作，因此對於新聞和時事文章的翻譯有深入的理解。我希望你能幫我將以下英文新聞段落翻譯成繁體中文，風格與上述雜誌的繁體中文版本相似。
​
規則：
​
- 翻譯時要準確傳達新聞事實和背景。
​
- 保留特定的英文術語或名字，並在其前後加上空格，例如："中 UN 文"。
​
- 分成兩次翻譯，並且打印每一次結果：
​
1. 根據新聞內容直譯，不要遺漏任何訊息
​
2. 根據第一次直譯的結果重新意譯，遵守原意的前提下讓內容更通俗易懂，符合台灣繁體中文的表達習慣
​
- 每輪翻譯後，都要重新比對英文原文，找到扭曲原意或者遺漏的內容，然後再補充到下一輪的翻譯當中。（Chain of Density 概念）
​
本條訊息只需要回覆 OK，接下來的訊息我將會給你發送完整內容，收到後請按照上面的規則打印兩次翻譯結果。
</Prompt>
```

#### 引用來源原文與相關說明：
<blockquote class="twitter-tweet"><p lang="zh" dir="ltr">《一个简单的Prompt大幅提升ChatGPT翻译质量，告别“机翻感”》<br><br>无论是Google翻译、DeepL翻译还是ChatGPT，翻译大段英文的时候，“机翻感”（机器翻译的感觉）都很强，一看就是机器翻译的，很生硬，但是自己手动润色又太费时间。… <a href="https://t.co/DpRZnovDTJ">https://t.co/DpRZnovDTJ</a> <a href="https://t.co/J6UFfCI0fo">pic.twitter.com/J6UFfCI0fo</a></p>&mdash; 宝玉 (@dotey) <a href="https://twitter.com/dotey/status/1707478347553395105?ref_src=twsrc%5Etfw">September 28, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2FminshiTsai%2Fposts%2Fpfbid02UcFLMJpuD1udovohFV2nNjnXZh9BycSvfDGQwngrdWJ6cYKRx1HpHTp7fAaSEMorl&show_text=true&width=500" width="500" height="608" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>

