sum_tickets = 0
qnt_tickets = int(input("Сколько билетов хотите приобрести?: "))
for age in range (qnt_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        sum_tickets +=0
    elif age >= 18 and age <= 25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1392

print ("Стоимость билетов:", sum_tickets, "руб.")

if qnt_tickets > 3:
    discount = sum_tickets / 100 * 10
    print("Скидка составляет:", "%.2f" % discount, "руб.")
    print("К оплате с учетом скидки:", "%.2f" % (sum_tickets -discount), "руб.")