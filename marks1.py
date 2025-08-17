dictionary={'alice': 85, 'bob': 90, 'charlie': 78,'ram': 92}
students = list(dictionary.keys())
students_names= input("Enter the names of student:")
if students_names in students:
    print(f"{students_names} has scored {dictionary[students_names]} marks.")
else:
    print(f"{students_names}  student name not found.")