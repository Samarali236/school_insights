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