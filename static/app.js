const form = document.getElementById("myForm");
// 當表單提交時觸發的事件處理函式
form.addEventListener("submit", function(event) {
    event.preventDefault(); // 防止表單的默認提交行為
    const inputText = document.getElementById("textInput").value;
    // Send user input text to backend
    $.ajax({
        url: '/palette',
        type: 'POST',
        data: {'query': inputText},
        success: function(response) {
            generatePalette(response);
        },
        error: function(error) {
            console.log(error); 
        }
    });

});

function generatePalette(responseArray) {
    const container = document.querySelector(".container");
    container.innerHTML = "";
    const colors = responseArray;
    for (const color of colors) {
        console.log(color);
        const div = document.createElement("div");
        const span = document.createElement("span");
        div.style.backgroundColor = color;
        div.style.width = `calc(100% / ${colors.length})`;
        div.classList.add("color-palette");
        div.innerHTML= `<span class="color-code-span">${color.toUpperCase()}</span>`;
        div.addEventListener("click", () => {
            navigator.clipboard.writeText(color);
        });
        container.appendChild(div);
    };
};
