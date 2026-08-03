students = ["张三","李四"]
students.append("王五")
students.remove("李四")
print(students)

numbers = [1,2,3,4,5,6,7]
print(numbers[:3])
print(numbers[3:])
print(numbers[-2:])

scores = [90,80,70,60]
for score in scores:
    print(f"成绩: {score}")

students = [["张三",90],["李四",80],["王五",70]]
for student in students:
    print(f"{student[0]}的成绩是{student[1]}")