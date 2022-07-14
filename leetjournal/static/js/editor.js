let editor = document.querySelector("#code");
let language = document.querySelector(".language")
console.log("hello")

editor.style.fontSize = '14px';
let codeEditor = ace.edit(editor);
codeEditor.setTheme("ace/theme/dracula");

language.addEventListener("change", function () {
    console.log("changed" + language.value)
    codeEditor.setValue("");
    codeEditor.session.setMode(`ace/mode/${language.value}`)
})

let form = document.querySelector(".solution-form")
let codeArea = document.querySelector("#script")

form.addEventListener("submit", () => {
    console.log("submitted")
    userCode = codeEditor.getValue();
    codeArea.value += userCode;
})

