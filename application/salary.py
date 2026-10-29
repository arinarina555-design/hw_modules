def calculate_salary():
    day_price = int(input("Введите сумму за день: "))
    salary = 21*day_price
    print(f"Зарплата за месяц: {salary}")
    return salary