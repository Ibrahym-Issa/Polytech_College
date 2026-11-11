function runTask3() {
    let num = parseInt(document.getElementById("task3Input").value);
    let result = document.getElementById("task3Result");
    if (isNaN(num)) {
        result.innerText = "Қате: Бүтін сан енгізіңіз!";
        return;
    }
    if (num % 2 === 0) {
        result.innerText = `${num} - жұп сан`;
    } else {
        result.innerText = `${num} - тақ сан`;
    }
}
