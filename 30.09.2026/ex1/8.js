function runTask8(mode) {
    let text = document.getElementById("task8Input").value;
    let result = document.getElementById("task8Result");
    if (mode === 'upper') {
        result.innerText = text.toUpperCase();
    } else {
        result.innerText = text.toLowerCase();
    }
}
