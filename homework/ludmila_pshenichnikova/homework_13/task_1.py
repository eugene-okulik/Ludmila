import os

import re

from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
new_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data2.txt')
print(eugene_file_path)


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


def process_date_action(date_str, action):
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    date = datetime.strptime(date_str, date_format)

    if "на неделю позже" in action:
        new_date = date + timedelta(weeks=1)
        return new_date.isoformat()
    elif "какой это будет день недели" in action:
        return date.strftime("%A")
    elif "сколько дней назад была эта дата" in action:
        now = datetime.now()
        days_ago = (now - date).days
        return f"{days_ago} дней назад"
    else:
        return "Неизвестное действие"


def main():
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        for data_line in read_file(eugene_file_path):
            match = re.match(r"(\d+)\.\s+([\d\-:\.\s]+)\s+-\s+(.+)", data_line)
            if match:
                number = match.group(1)
                date_str = match.group(2).strip()
                action = match.group(3).strip()

                result = process_date_action(date_str, action)
                new_file.write(f"Строка {number}: {result}\n")


if __name__ == "__main__":
    main()
