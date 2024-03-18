def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None

    except Exception as e:
        print(f"Помилка: {e}")
        return None

    if count > 0:
        average_salary = total / count

    else:
        average_salary = 0

    return total, average_salary


total_result = total_salary('salary.txt')
if total_result is not None:
    total, average = total_result
    print(f"Загальна заробітна плата: {total}")
    print(f"Середня заробітна плата: {average}")
