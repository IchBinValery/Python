# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


print ("Загадай число")

A = input()

B = A+A

C = B+A

D = (int (A)+int (B)+int (C))

print ("Так вышло что ответ: ", D)

input('Press ENTER to exit')