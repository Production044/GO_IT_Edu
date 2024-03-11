from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()  # Поточна дата
    upcoming_birthdays = []  # Порожній список для зберігання інформації про наближені дні народження

    for user in users:
        birthday = datetime.strptime(user["birthday"],
                                     "%Y.%m.%d").date()  # Конвертуємо день народження з рядка у об'єкт datetime
        birthday_this_year = birthday.replace(year=today.year)  # День народження в поточному році

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)  # Якщо день народження вже пройшов у поточному році, переносимо його на наступний рік

        days_until_birthday = (
                    birthday_this_year - today).days  # Визначаємо кількість днів до наступного дня народження

        if days_until_birthday <= 7:  # Якщо день народження випадає протягом наступного тижня
            if days_until_birthday == 0:
                congratulation_date = today  # Якщо день народження сьогодні, привітання буде сьогодні
            elif birthday_this_year.weekday() in [5, 6]:  # Якщо день народження випадає на вихідні
                congratulation_date = birthday_this_year + timedelta(
                    days=(7 - birthday_this_year.weekday()))  # Переносимо привітання на наступний понеділок
            else:
                congratulation_date = birthday_this_year  # Інакше залишаємо дату привітання без змін

            # Додаємо інформацію про користувача та дату привітання у список
            upcoming_birthdays.append(
                {"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays


# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.03.17"},
    {"name": "Jane Smith", "birthday": "1990.03.16"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
