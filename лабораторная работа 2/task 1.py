money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = -1
i = 0
cash = 1
while cash > 0:
    buy = spend * (1 + increase) ** i
    cash = money_capital + salary - buy
    money_capital += salary - buy
    months += 1
    i += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
