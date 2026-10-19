const tableBody = document.getElementById("tasks-table-body");
const statusFilter = document.getElementById("status-filter");

let allTasks = [];

document.addEventListener("DOMContentLoaded", loadTasks);


async function loadTasks() {
    try {
        const response = await fetch("/tasks");

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || "Failed to load tasks");
        }

        if (!Array.isArray(data.tasks)) {
            throw new Error("The server did not return a valid task list");
        }

        allTasks = data.tasks;

        displayTasks(allTasks);
        updateSummaryCards(allTasks);

    } catch (error) {
        console.error("Error loading tasks:", error);

        tableBody.replaceChildren();

        const row = document.createElement("tr");
        const cell = document.createElement("td");

        cell.colSpan = 7;
        cell.textContent =
            "Unable to load tasks. Check your Flask server and try again.";

        row.appendChild(cell);
        tableBody.appendChild(row);
    }
}


function displayTasks(tasks) {
    tableBody.replaceChildren();

    if (tasks.length === 0) {
        const row = document.createElement("tr");
        const cell = document.createElement("td");

        cell.colSpan = 7;
        cell.textContent = "No tasks found.";

        row.appendChild(cell);
        tableBody.appendChild(row);

        return;
    }

    tasks.forEach(function(task) {
        const row = document.createElement("tr");

        const values = [
            task.title,
            task.client,
            task.recipient,
            task.priority,
            task.status,
            task.due_date
        ];

        values.forEach(function(value) {
            const cell = document.createElement("td");

            cell.textContent = value ?? "—";

            row.appendChild(cell);
        });

        const actionCell = document.createElement("td");

        actionCell.textContent = "—";

        row.appendChild(actionCell);

        tableBody.appendChild(row);
    });
}


function updateSummaryCards(tasks) {
    document.getElementById("total-count").textContent = tasks.length;

    document.getElementById("pending-count").textContent =
        tasks.filter(function(task) {
            return task.status === "Pending";
        }).length;

    document.getElementById("completed-count").textContent =
        tasks.filter(function(task) {
            return task.status === "Completed";
        }).length;
}


statusFilter.addEventListener("change", function() {
    const selectedStatus = statusFilter.value;

    const filteredTasks = selectedStatus === "All"
        ? allTasks
        : allTasks.filter(function(task) {
            return task.status === selectedStatus;
        });

    displayTasks(filteredTasks);
});