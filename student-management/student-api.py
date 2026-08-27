from fastapi import FastAPI
app = FastAPI()


students = ["Rahul","Priya","Arjun","Sneha","Kiran"]  
marks = [78,92,65,88,74]
courses = ["Python","FastAPI","SQL","Python","SQL"]
attendance = [85,92,68,95,78]

@app.get("/students")          
def students_data():
    data = []
    for i in range(len(students)):
        data.append({
            "student-name": students[i],
            "marks": marks[i],
            "attendance": attendance[i],
            "courses": courses[i]
        })
    return data

@app.get("/students/{student_name}")          
def student_search(student_name: str):
    if student_name in students:
        index=students.index(student_name)
        return{
            "name":students[index],
            "marks":marks[index],
            "course": courses[index],
            "attendance": attendance[index]
        }
    else:
         return f"{student_name} details not found"

@app.put("/students/{student_name}")
def update_marks(student_name: str, new_marks: int):
    if student_name in students:
        index=students.index(student_name)
        marks[index]=new_marks
        return f"{student_name}'s marks updated sucessfully . . ."  
    else:
        return f"{student_name} details not found" 

@app.put("/students/{student_name}/attendance")
def update_attendance(student_name: str, new_attendance: int):
    if student_name in students:
        index=students.index(student_name)
        attendance[index]=new_attendance
        return f"{student_name}'s attenadance updated sucessfully . . ."  
    else:
        return f"{student_name} details not found"

@app.delete("/students/{student_name}")
def student_delete(student_name: str):
    if student_name in students:
        index=students.index(student_name)
        students.remove(student_name)
        marks.pop(index)
        courses.pop(index)
        attendance.pop(index)
        return f"{student_name} details deleted successfully"  
    else: 
        return f"{student_name} details not found"

@app.post("/students/{student_name}")
def new_student(student_name: str,student_marks: int,student_attendance: int,student_course: str):
    if student_name not in students:
        students.append(student_name)
        marks.append(student_marks)
        courses.append(student_course)
        attendance.append(student_attendance)
        return f"{student_name} details added successfully"
    else:
        return f"{student_name} already exists"
