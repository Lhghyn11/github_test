colors = ("red","green","blue")
print(colors[0])
print(len(colors))

numbers = [1,2,2,3,3,4]
numbers = set(numbers)
print(numbers)

text = " Hello Python"
print(text.strip())
print(text.upper())

sentence = "I love Python"
print(sentence.split())
print(len(sentence.split()))

sentence = "I love Python"
words = sentence.split()
print(words)
print(len(words))

text = "I love Java"
text = text.replace("Java","Python")
print(text)

sentence = "I love Python"
print(sentence.find("Python"))
print(sentence.find("Java"))