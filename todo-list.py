import streamlit as st
import json
import os

# File to store tasks
TODO_FILE = "todo.json"

# Function to load tasks from the file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        # Create the file and initialize it with an empty list
        with open(TODO_FILE, "w") as file:
            json.dump([], file)
    with open(TODO_FILE, "r") as file:
        return json.load(file)

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Styling for the app
st.markdown(
    """
    <style>
    .done {
        text-decoration: line-through;
        color: gray;
        font-size: 1.1em;
    }
    .not-done {
        font-weight: bold;
        color: #1a73e8;
        font-size: 1.2em;
    }
    .priority-high {
        color: red;
        font-weight: bold;
    }
    .priority-medium {
        color: orange;
    }
    .priority-low {
        color: green;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the application
st.title("✨ To-Do List Manager")
st.write("Organize your tasks efficiently!")

# Task operations
tasks = load_tasks()

# Add a task with priority
st.subheader("Add a New Task")
new_task = st.text_input("Task Description:")
priority = st.selectbox("Priority", ["High", "Medium", "Low"])
if st.button("Add Task", key="add-task"):
    if new_task.strip():
        tasks.append({"task": new_task.strip(), "completed": False, "priority": priority})
        save_tasks(tasks)
        st.success(f"Task added successfully: {new_task}")
        #  # Reloads the app to show updated task list

# List tasks
if tasks:
    st.subheader("Your Tasks")
    for index, task in enumerate(tasks):
        col1, col2, col3 = st.columns([6, 2, 2])
        with col1:
            task_style = "done" if task["completed"] else "not-done"
            priority_class = f"priority-{task['priority'].lower()}"
            st.markdown(
                f'<span class="{task_style}">{task["task"]}</span> '
                f'<span class="{priority_class}">({task["priority"]} Priority)</span>',
                unsafe_allow_html=True,
            )
        with col2:
            if not task["completed"] and st.button("Mark as Done", key=f"done-{index}"):
                task["completed"] = True
                save_tasks(tasks)
                # # Reloads the app to reflect changes
        with col3:
            if st.button("Remove Task", key=f"remove-{index}"):
                tasks.pop(index)
                save_tasks(tasks)
               #  # Reloads the app to reflect changes
else:
    st.info("No tasks found. Add a new task to get started!")

# Footer
st.markdown("---")
st.markdown("✨ Develop By UMAR KHAN  ✨")
