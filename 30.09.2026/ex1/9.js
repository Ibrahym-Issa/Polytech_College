let totalSeconds = 0;
let timerInterval = null;

function formatTime(seconds) {
    let mins = Math.floor(seconds / 60);
    let secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

function startTimer() {
    if (timerInterval !== null) return;
    document.getElementById("timerCircle").classList.add("running");
    timerInterval = setInterval(() => {
        totalSeconds++;
        document.getElementById("timerCircle").innerText = formatTime(totalSeconds);
    }, 1000);
}

function pauseTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
    document.getElementById("timerCircle").classList.remove("running");
}

function resetTimer() {
    pauseTimer();
    totalSeconds = 0;
    document.getElementById("timerCircle").innerText = "00:00";
}
