tasks = {
    "Python": "Completed",
    "SQL": "Pending",
    "Git": "Completed",
    "FastAPI": "Pending"
}

completed = 0

for task, status in tasks.items():
    if status == "Completed":
        completed += 1

print("Completed tasks:", completed)