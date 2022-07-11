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
