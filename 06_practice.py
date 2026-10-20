students = {
    "Rudra": 80,
    "Rahul": 65,
    "Amit": 90
}

for name, marks in students.items():
    if marks >= 70:
        print(name, "passed")