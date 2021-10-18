// 번호는 1부터 100까지 입력!!!
function wrongNumber(nInput)/*: bool*/ {
    const todo = document.getElementById("todo");
    if (0 < nInput && nInput < 101 && nInput < todo.children.length + 1) {
        return true;
    } else {
        alert("번호를 다시 입력하세요.");
        return false;
    }
}
