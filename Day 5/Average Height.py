student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)

total_height = 0

for height in student_heights:
    total_height += height
# print(total_height)

total_students = 0

for student in student_heights:
    total_students += 1
# print(total_students)

average_height = round(total_height / total_students)
print(f"Average height of students is {average_height}")