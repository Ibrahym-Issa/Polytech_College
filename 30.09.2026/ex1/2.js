function runTask2() {
    let name = document.getElementById("task2Input").value.trim();
    let result = document.getElementById("task2Result");
    if(name) {
        result.innerText = `Қош келдіңіз, ${name}!`;
    } else {
        result.innerText = "Есімді енгізіңіз!";
    }
}
