"""6. Дано ціле число в діапазоні 1-7. Вивести рядок - назва дня тижня, що відповідає даному числу (1 -
«понеділок», 2 - «вівторок» і т. д.).
"""

a = int(input("Число от 1-7 "))

if a > 7 or a < 1:
    print("Неправильный ввод")
    exit(1)

match a :
 case 1 :
    print("Понедельник")
 case 2:
    print("Вторник")
 case 3:
    print("Среда")
 case 4 :
    print("Четверг")
 case 5:
    print("Пятница")
 case 6:
    print("Суббота")
 case 7:
    print("Воскресенье")
