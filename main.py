from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    anniversaries = {}
    cur_date = date.today()
    for user in users:
        bd = user["birthday"]
        if cur_date.weekday() == 0:
            for i in range(3):
                cur_d_tmp = cur_date - timedelta(days=i)
                bd = datetime(cur_d_tmp.year, bd.month, bd.day).date()
                if bd == cur_d_tmp:
                    anniv_tmp = anniversaries.get(day_of_week[0], [])
                    anniv_tmp.append(user["name"])
                    anniversaries[day_of_week[0]] = anniv_tmp
                    break
            for i in range(1, 5):
                cur_d_tmp = cur_date + timedelta(days=i)
                bd = datetime(cur_d_tmp.year, bd.month, bd.day).date()
                if bd == cur_d_tmp:
                    anniv_tmp = anniversaries.get(day_of_week[bd.weekday()], [])
                    anniv_tmp.append(user["name"])
                    anniversaries[day_of_week[bd.weekday()]] = anniv_tmp
                    break
        else:
            for i in range(7):
                cur_d_tmp = cur_date + timedelta(days=i)
                bd = datetime(cur_d_tmp.year, bd.month, bd.day).date()
                cur_week_day = cur_d_tmp.weekday()
                if cur_week_day in [0, 5, 6]:
                    cur_week_day = 0
                if bd == cur_d_tmp:
                    anniv_tmp = anniversaries.get(day_of_week[cur_week_day], [])
                    anniv_tmp.append(user["name"])
                    anniversaries[day_of_week[cur_week_day]] = anniv_tmp
                    break

    return anniversaries


if __name__ == "__main__":
    users = [
        {"name": "Natan Koum 23", "birthday": datetime(1976, 8, 30).date()},
        {"name": "Mike Koum 23", "birthday": datetime(1976, 12, 30).date()},

        {"name": "Greg Koum 23", "birthday": datetime(1971, 12, 31).date()},

        {"name": "Jan Koum 24", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Gog Koum 24", "birthday": datetime(1971, 1, 2).date()},
        {"name": "Mike Koum 24", "birthday": datetime(1976, 1, 3).date()},
        {"name": "Kola Koum 24", "birthday": datetime(1976, 1, 4).date()},
        {"name": "Pet Koum 24", "birthday": datetime(1976, 1, 5).date()},
        {"name": "Jude Koum 24", "birthday": datetime(1976, 1, 6).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
