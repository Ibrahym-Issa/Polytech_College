function runTask7() {
    let dist = parseFloat(document.getElementById("task7Dist").value);
    let price = parseFloat(document.getElementById("task7Price").value);
    let result = document.getElementById("task7Result");

    if(isNaN(dist) || isNaN(price) || dist < 0 || price < 0) {
        result.innerText = "Қате мәлімет!";
        return;
    }
    result.innerText = `Жалпы құны: ${dist * price} тг`;
}
