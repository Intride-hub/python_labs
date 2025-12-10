from src.lab08.serialize import students_from_json, students_to_json

input_path = "data/lab08/students_input.json"
output_path = "data/lab08/students_output.json"

students = students_from_json(input_path)

for s in students:
    print(s, "| возраст:", s.age())

students_to_json(students, output_path)
print("\nСериализация завершена. Файл сохранён в", output_path)
