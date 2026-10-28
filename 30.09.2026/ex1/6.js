function runTask6() {
    let input = document.getElementById("task6Input");
    let taskText = input.value.trim();
    if(taskText) {
        let li = document.createElement("li");
        li.innerText = taskText;
        document.getElementById("task6List").appendChild(li);
        input.value = "";
    }
}
