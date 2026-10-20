// console.log("Hello, JavaScript");
// ---------- DAY 3: JavaScript ----------

// 1. Grab the elements we need from the page
const taskForm = document.getElementById("taskForm");
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");
const emptyMessage = document.getElementById("emptyMessage");
const totalCount = document.getElementById("totalCount");
const doneCount = document.getElementById("doneCount");
const progressFill = document.getElementById("progressFill");
const colorPicker = document.getElementById("colorPicker");

// 2. Load saved tasks from the browser (or start with an empty list)
let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

// 3. Save tasks to the browser
function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

// 4. Show everything on the screen
function render() {
  taskList.innerHTML = "";

  tasks.forEach(function (task) {
    const li = document.createElement("li");
    li.className = "task" + (task.done ? " done" : "");

    // checkbox to mark complete
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.done;
    checkbox.addEventListener("change", function () {
      toggleTask(task.id);
    });

    // the task text
    const span = document.createElement("span");
    span.className = "task-text";
    span.textContent = task.text;

    // delete button
    const deleteBtn = document.createElement("button");
    deleteBtn.className = "delete-btn";
    deleteBtn.textContent = "✕";
    deleteBtn.setAttribute("aria-label", "Delete task");
    deleteBtn.addEventListener("click", function () {
      deleteTask(task.id);
    });

    li.append(checkbox, span, deleteBtn);
    taskList.appendChild(li);
  });

  updateStats();
}

// 5. Count tasks and update the progress bar
function updateStats() {
  const total = tasks.length;
  const done = tasks.filter(function (task) {
    return task.done;
  }).length;

  totalCount.textContent = total;
  doneCount.textContent = done;

  const percent = total === 0 ? 0 : (done / total) * 100;
  progressFill.style.width = percent + "%";

  emptyMessage.style.display = total === 0 ? "block" : "none";
}

// 6. Add a task
function addTask(text) {
  tasks.push({
    id: Date.now(),
    text: text,
    done: false
  });
  saveTasks();
  render();
}

// 7. Mark complete or incomplete
function toggleTask(id) {
  tasks = tasks.map(function (task) {
    if (task.id === id) {
      return { id: task.id, text: task.text, done: !task.done };
    }
    return task;
  });
  saveTasks();
  render();
}

// 8. Delete a task
function deleteTask(id) {
  tasks = tasks.filter(function (task) {
    return task.id !== id;
  });
  saveTasks();
  render();
}

// 9. When the form is submitted, add the task
taskForm.addEventListener("submit", function (event) {
  event.preventDefault(); // stop the page from reloading
  const text = taskInput.value.trim();
  if (text === "") return;
  addTask(text);
  taskInput.value = "";
  taskInput.focus();
});

// 10. Theme colour: change the CSS variable and remember it
function applyColor(color) {
  document.documentElement.style.setProperty("--accent", color);
  colorPicker.value = color;
  localStorage.setItem("themeColor", color);
}

colorPicker.addEventListener("input", function () {
  applyColor(colorPicker.value);
});

const savedColor = localStorage.getItem("themeColor");
if (savedColor) {
  applyColor(savedColor);
}

// 11. First draw when the page opens
render();