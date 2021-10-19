// 새로운계획 추가하기 버튼 클릭시
document.getElementById("Text_input_Button").addEventListener("click", addSchedule);
function addSchedule() {
    let value = document.getElementById("Text_input").value; // 입력되는 값
    let todo = document.getElementById("todo");
    const li = document.createElement("li");
    li.innerHTML = value; // 입력되는값 li로
    if (!noInputSchedule(value)) {
        todo.appendChild(li);  // li ol태그의 자식으로 추가
        alert("\'" + value + "\' 계획을 추가합니다.");
    }
}

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
// 텍스트 비어있을때 리스트 항목 추가 할 수 없음 알림메시지
function noInputSchedule(strInput) {
    if (!strInput) {
        alert("계획을 다시 입력하세요.");
        return true;
    }
    return false;
}
// modify
document.getElementById("modify-btn").addEventListener("click", (event) => {
    const numInput = document.getElementById("num").value;
    const strInput = document.getElementById("after").value;
    event.preventDefault();
    const nInput = parseInt(numInput);
    if (wrongNumber(nInput)) {
        if (!noInputSchedule(strInput)) {
            const target = document.getElementById("todo").children.item(nInput - 1);
            target.innerHTML = strInput;
            alert(numInput + "번 항목을 \'" + strInput + "\'로 수정합니다.");
        }
    }
});
