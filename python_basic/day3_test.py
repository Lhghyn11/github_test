for i in range(1,6):
    print(i)

total = 0
for i in range(1,101):
    total += i
print(total)

students = ["张三","李四","王五"]
for student in students:
    print(student)

scores = [90,80,70]
total = 0
for score in scores:
    total += score
average = total / 3
print(average)

life = 5
while life > 0:
    print(life)
    life -= 1
print("开始！")

for i in range(10):
    if i ==5:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(1,11):
    if i ==5:
        break
    print(i)

