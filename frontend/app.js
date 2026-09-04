async function loadTasks(){
	const response = await fetch("/api/tasks");
	const tasks = await response.json();

	const list = document.getElementById("tasks");
	list.innerHTML = "";
	tasks.forEach( task => {
		const item = document.createElement("li");
		item.textContent = `${task["Serial No."]} | ${task.Title} | Completed: ${task.Completed}`;
		list.appendChild(item);
		});
}


async function addTask(){
	const input = document.getElementById("taskTitle");
	const title = input.value.trim();
	
	if (title === ""){
		alert("Please Enter a Task");
	return;
	}
	
	const response = await fetch("/api/tasks",{ method : "POST", 
		headers : {"Content-type" : "application/json"}, 
		body : JSON.stringify({
		Title:title
		})
		});

	  if (!response.ok) {
       	 	alert("Failed to add task");
        	return;
    	}

    	input.value = "";
    	await loadTasks();
}
