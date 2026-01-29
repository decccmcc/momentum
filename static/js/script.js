
document.addEventListener("DOMContentLoaded", function () {
        var toastElList = [].slice.call(document.querySelectorAll(".toast"));
        var toastList = toastElList.map(function (toastEl) {
          var toast = new bootstrap.Toast(toastEl);
          toast.show();
          return toast;
        })

      })


function openAddModal() {
    // Reset modal title and button
    document.getElementById("addTaskModalLabel").innerText = "Add New Task";
    document.getElementById("taskSubmitBtn").innerText = "Save Task";
    
    // Set form action to add
    document.getElementById("taskForm").action = "{% url 'task_add' %}";

    // Clear all fields
    document.getElementById("id_title").value = "";
    document.getElementById("id_description").value = "";
    document.getElementById("id_due_date").value = "";
    document.getElementById("id_priority").value = "medium";
    document.getElementById("id_status").value = "pending";
    document.getElementById("id_category").value = "personal";
}

function openEditModal(id, title, description, due_date, priority, status, category) {
    // Change modal title and button
    document.getElementById("addTaskModalLabel").innerText = "Edit Task";
    document.getElementById("taskSubmitBtn").innerText = "Update Task";
    
    // Set form action to edit
    document.getElementById("taskForm").action = "{% url 'task_edit' 0 %}".replace('0', id);

    // Fill fields with task data
    document.getElementById("id_title").value = title;
    document.getElementById("id_description").value = description;
    document.getElementById("id_due_date").value = due_date;
    document.getElementById("id_priority").value = priority;
    document.getElementById("id_status").value = status;
    document.getElementById("id_category").value = category;
}