def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(',')
                cats_list.append({'id: ': cat_id, 'name: ': cat_name, 'age: ': cat_age})

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None

    except Exception as e:
        print(f"Помилка: {e}")
        return None

    return cats_list


cats_list = get_cats_info('Cats.txt')
if cats_list is not None:
    print(cats_list)
