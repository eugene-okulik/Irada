import os
import re
from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)
# print(base_path)
hmw_path = os.path.dirname(os.path.dirname(base_path))
# print(hmw_path)
hw13_path = os.path.join(hmw_path, 'eugene_okulik', 'hw_13', 'data.txt')
# print(hw13_path)

# with open(hw13_path) as data_file:
#     print(data_file.read())
#
# now = datetime.now()
# print(now)


def process_date(line):
    my_pattern = r'(\d+)\.\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\s+-\s+(.+)'
    match = re.match(my_pattern, line)

    number = match.group(1)
    date_str = match.group(2)
    action = match.group(3).strip()

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

        if "распечатать эту дату, но на неделю позже" in action:
            new_date = date_obj + timedelta(weeks=1)
            print(f"{number}. {new_date.strftime('%Y-%m-%d %H:%M:%S.%f')}")

        elif "распечатать какой это будет день недели" in action:
            day_of_week = date_obj.strftime('%A')
            print(f"{number}. {day_of_week}")

        elif "распечатать сколько дней назад была эта дата" in action:
            now = datetime.now()
            days_ago = (now - date_obj).days
            print(f"{number}. {days_ago}")


    except ValueError as e:
        print(f"{number}. Time or Date errors: {e}")


def main():
    try:
        with open(hw13_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    process_date(line)

    except FileNotFoundError:
        print("Cannot find data.txt")
    except Exception as e:
        print(f"Cannot open: {e}")


if __name__ == "__main__":
    main()
