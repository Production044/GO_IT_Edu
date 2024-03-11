from datetime import datetime


def get_days_from_today(date):
    current_datetime = datetime.today()
    another_datetime = datetime.strptime(date, "%Y-%m-%d")
    total_days = current_datetime.toordinal() - another_datetime.toordinal()
    return print(f'Current date time: {current_datetime} \n'
                 f'Another date time: {another_datetime} \n'
                 f'Total days: {total_days}')


get_days_from_today('2019-10-09')