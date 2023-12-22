"""
1.  Напишіть функцію для перевірки чи є послідовність цілих
чисел арифметичною прогресією чи ні. Примітка. У математиці
арифметична прогресія або арифметична послідовність - це послідовність чисел,
в якій різниця між послідовними членами є постійною. Наприклад, послідовність 5, 7, 9, 11, 13, 15,...
є арифметичною прогресією із загальною різницею 2.
Вхідні дані:
5 7 9 11
5 7 10 12
Вихідні дані:
True
False


Автор: Шарабар Ярослав Анатолійович

"""
def func(sequence):
    if len(sequence) < 3:
        return False
    
    
    
    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i-1] != difference:
            return False
    
    return True
difference = sequence[1] - sequence[0]

text = input("Введіть послідовність чисел через пробіл: ")

numbers = text.split()
for l in range(len(numbers)):
    numbers[l] = int(numbers[l])

if func(numbers):
    print("true")
else:
    print("false")
