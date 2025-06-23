records = [
["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
["Jana", 94], ["Ziad", 75]
]

#Rebuilding the journal:

class_journal={}

for name, grade in records:
    if name in class_journal:
        class_journal[name].append(grade)
    else:
        class_journal[name]=[grade]
        

#The basic Report:

def find_avg():
    for name in class_journal:
        grade=class_journal[name]
        avg=sum(grade)/len(grade)
        class_journal[name] = {
        "grades": grade,
        "average": round(avg,2)
    }  
        print(f"The Data List of: {name} is :{class_journal[name]}, The Average is : {round(avg,2)}")
      
find_avg()

#Deeper Analysis

#highest average
max_avg=0
student_maxavg=""
for name in class_journal:
    average=class_journal[name]["average"]
    if average>max_avg:
         max_avg=average
         student_maxavg=name
print(f"The students with the Highest average is {student_maxavg} with an average of {max_avg}")

#most consistent
diff_list=[]
name_list=[]
const_student=""
for name in class_journal:
    grades=class_journal[name]["grades"]
    max_grade=grades[0]
    min_grade=grades[0]
    for i in range(1,len(grades)):
        if max_grade<grades[i]:
            max_grade=grades[i]
        elif min_grade>grades[i]:
            min_grade=grades[i]
    difference=max_grade-min_grade
    diff_list.append(difference)
    name_list.append(name)

min_diff=diff_list[0]
const_student=name_list[0]
for i in range(1,len(diff_list)):
    if min_diff>diff_list[i]:
        min_diff=diff_list[i]
        const_student=name_list[i]
print(f"The List of grade Differences is {diff_list}")
print(f"the student with the most consistent performance is :{const_student} ,grade difference:{min_diff}")

#student who had at least one grade below 70
below70_student=[]
for name in class_journal:
    grades=class_journal[name]["grades"]
    for i in range(len(grades)):
        if grades[i]<70:
            below70_student.append(name)
print(f"The list of students who had at least one grade below 70 is : {below70_student}")