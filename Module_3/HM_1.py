from datetime import datetime


def get_days_from_today(date):
    try:
        current_datetime = datetime.today()
        another_datetime = datetime.strptime(date, "%Y-%m-%d")
        total_days = current_datetime.toordinal() - another_datetime.toordinal()
        print(total_days)
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'.")


get_days_from_today('2000-10-09')