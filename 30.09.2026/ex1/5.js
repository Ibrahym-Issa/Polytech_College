function runTask5(operation) {
    let n1 = parseFloat(document.getElementById("task5Num1").value);
    let n2 = parseFloat(document.getElementById("task5Num2").value);
    let result = document.getElementById("task5Result");

    // Проверка на заполненность полей
    if (isNaN(n1) || isNaN(n2)) {
        result.innerText = "Қате: Сандарды толық енгізіңіз!";
        return;
    }

    let res = 0;

    switch (operation) {
        case '+':
            res = n1 + n2;
            break;
        case '-':
            res = n1 - n2;
            break;
        case '*':
            res = n1 * n2;
            break;
        case '/':
            // Проверка деления на ноль
            if (n2 === 0) {
                result.innerText = "Нөлге бөлу мүмкін емес!";
                return;
            }
            res = n1 / n2;
            break;
        default:
            result.innerText = "Белгісіз операция!";
            return;
    }

    result.innerText = `Нәтиже: ${res}`;
}
