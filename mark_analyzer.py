marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

average = sum(marks) / n
highest = max(marks)
lowest = min(marks)

print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
