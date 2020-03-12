# gradebook.py

# Display the average of each student's grade.
# Display tthe average for each assignment.

gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]



student0 = gradebook[0]
student1 = gradebook[1]
student2 = gradebook[2]
student3 = gradebook[3]
student4 = gradebook[4]
student5 = gradebook[5]
student6 = gradebook[6]
student7 = gradebook[7]
student8 = gradebook[8]
student9 = gradebook[9]

studentList = []

studentList.append(student0)
studentList.append(student1)
studentList.append(student2)
studentList.append(student3)
studentList.append(student4)
studentList.append(student5)
studentList.append(student6)
studentList.append(student7)
studentList.append(student8)
studentList.append(student9)



rowSum =0
studentAverage = 0
studentAverageList = []

for row in gradebook:
    studentAverage = 0
    rowSum =0
    for element in row:
        rowSum += element
    studentAverage = rowSum/15
    studentAverageList.append(studentAverage)

assignmentAverage = []
assignmentSum = []
i = 0
# for row in gradebook:
  #  assignmentSum += row[i]
    # print(assignmentSum)
for i in range(0,14):
    a = [row[i] for row in gradebook]
    assignmentSum.append(sum(a))
print("Assignment Averages:")
for i in range(0,14):
    assignmentAverage.append(assignmentSum[i]/10)    
    print("Assignment"+ str(i+1) + ": " + str(assignmentAverage[i]))

    


print("Student Averages:")
i = 0
for row in gradebook:
    print("Student"+ str(i) + ": "+ str(studentAverageList[i]))
    i += 1


        
