from datetime import datetime


def get_days_from_today(date):
    try:
        current_datetime = datetime.today()
        another_datetime = datetime.strptime(date, "%Y-%m-%d")
        total_days = current_datetime.toordinal() - another_datetime.toordinal()
        return total_days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'."


print(get_days_from_today('220-10-09'))