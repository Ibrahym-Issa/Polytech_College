// Загрузка сохраненных задач при старте страницы
document.addEventListener("DOMContentLoaded", loadTasks);

function getTasksFromStorage() {
    return JSON.parse(localStorage.getItem("tasks")) || [];
}

function saveTasksToStorage(tasks) {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function addTask10() {
    let input = document.getElementById("task10Input");
    let prioritySelect = document.getElementById("task10Priority");
    
    let text = input.value.trim();
    let priority = prioritySelect.value;
    
    if (!text) return;

    let tasks = getTasksFromStorage();
    tasks.push({ text: text, priority: priority, id: Date.now() });
    
    saveTasksToStorage(tasks);
    input.value = "";
    renderTasks();
}

function deleteTask10(id) {
    let tasks = getTasksFromStorage();
    tasks = tasks.filter(t => t.id !== id);
    saveTasksToStorage(tasks);
    renderTasks();
}

function clearAllTasks() {
    if(confirm("Шын мәнінде барлық тапсырмаларды өшіргіңіз келе ме?")) {
        saveTasksToStorage([]);
        renderTasks();
    }
}

function renderTasks() {
    let ul = document.getElementById("task10List");
    ul.innerHTML = "";
    let tasks = getTasksFromStorage();

    tasks.forEach(task => {
        let li = document.createElement("li");
        li.className = task.priority; // Добавит класс 'high' или 'normal'
        
        li.innerHTML = `
            <span>${task.text} ${task.priority === 'high' ? '<strong>(!!!)</strong>' : ''}</span>
            <i class="fa-solid fa-trash-can delete-ico" onclick="deleteTask10(${task.id})"></i>
        `;
        ul.appendChild(li);
    });

    document.getElementById("task10Count").innerText = `Барлығы: ${tasks.length} тапсырма`;
}

function loadTasks() {
    renderTasks();
}
