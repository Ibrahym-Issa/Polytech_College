function changeBoxColor(color) {
    let box = document.getElementById("colorBox");
    
    // Эффектно меняем фон самого документа (body)
    if(color === 'red') document.body.style.backgroundColor = "#ffe3e3";
    if(color === 'green') document.body.style.backgroundColor = "#e3ffe7";
    if(color === 'blue') document.body.style.backgroundColor = "#e3f0ff";
    
    box.style.backgroundColor = color;
    box.style.color = "white";
    box.style.borderColor = "transparent";
    box.innerText = `Ағымдағы түс: ${color.toUpperCase()}`;
}
