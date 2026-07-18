student = {
    "name": "Bhavith Sai",
    "age": 17,
    "course": "MPC"
}

print("===== Original Dictionary =====")
print(student)

# Update age
student["age"] = 18

# Add a new key
student["college"] = "Sri Chaitanya"

print("\n===== Updated Dictionary =====")

for key, value in student.items():
    print(key.capitalize() + ":", value)