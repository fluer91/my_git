number = int(input())
print("Четное" if number % 2 == 0 else "Нечетное")

a, b, c = map(int, input().split())
print(max(a, b, c))

number = int(input())
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

Cozdor = "аеёиоуэыюя"
text = input().lower()
count = sum(1 for char in text if char in Cozdor)
print(count)

n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

word = input().lower()
if word == word[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")

total = 0
for _ in range(5):
    total += int(input())
print(total)

sentence = input()
words = sentence.split()
print(len(words))

def square(x):
    return x ** 2
number = int(input())
print(square(number))

def minimum(a, b):
    return a if a < b else b

x = int(input())
y = int(input())
print(minimum(x, y))

def is_even(number):
    return number % 2 == 0

num = int(input())
print(is_even(num))

def count_vowels(text):
    vowels = "аеёиоуэыюя"
    return sum(1 for char in text.lower() if char in vowels)

input_text = input()
print(count_vowels(input_text))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input())
print(factorial(n))

def average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(int, input().split()))
print(average(numbers))

def is_palindrome(s):
    return s == s[::-1]

text = input()
print(is_palindrome(text))

def count_words(text):
    return len(text.split())

sentence = input()
print(count_words(sentence))