school_grades = [
["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
["Jana", 94], ["Ziad", 75]
]

#Rebuilding the journal:
def school_insights(records):
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
    output1=f"The students with the Highest average is {student_maxavg} with an average of {max_avg}"

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
    output2=f"The List of grade Differences is {diff_list} the student with the most consistent performance is :{const_student} ,grade difference:{min_diff}"

    #student who had at least one grade below 70
    below70_student=[]
    for name in class_journal:
        grades=class_journal[name]["grades"]
        for i in range(len(grades)):
            if grades[i]<70:
                below70_student.append(name)
    output3=f"The list of students who had at least one grade below 70 is : {below70_student}"

    #total grades were entered across the whole class:
    output4=f"The total grades entered across the whole class is: {len(records)} Grades "

    #overall class average:
    overall_avg=[]
    for name in class_journal:
        average=class_journal[name]["average"]
        overall_avg.append(average)
        overall_average=sum(overall_avg)/len(overall_avg)
        output5=f"The overall class average is : {overall_average}"

    #generating a text file having the requirment
    print(output1)
    print(output2)
    print(output3)
    print(output4)
    print(output5)

    with open("class_report.txt", "w") as f:
        f.write(output1 + "\n")
        f.write(output2 + "\n")
        f.write(output3 + "\n")
        f.write(output4 + "\n")
        f.write(output5 + "\n")

school_insights(school_grades)

#adding more data to school_grades list
school_grades = school_grades + [["Jana", 99], ["Ziad", 78], ["Layla", 84]]

#rerunning the whole analysis
school_insights(school_grades)


