function analyze() {
    const input = document.getElementById("taskInput").value;

    let tasksData;
    try {
        tasksData = JSON.parse(input);   // Parse user JSON text
    } catch (e) {
        alert("Invalid JSON format");
        return;
    }

    fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ tasks: tasksData })
    })
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById("result");
        container.innerHTML = "";

        if (!data.results) {
            container.innerHTML = "<p>No results returned</p>";
            return;
        }

        data.results.forEach(task => {
            const div = document.createElement("div");
            div.className = "task-card";
            div.innerHTML = `
                <h3>${task.title}</h3>
                <p>Score: ${task.score}</p>
                <p>Due: ${task.due_date}</p>
                <p>Importance: ${task.importance}</p>
            `;
            container.appendChild(div);
        });
    });
}
