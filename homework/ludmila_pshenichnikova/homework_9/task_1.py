import datetime

data = 'Jan 15, 2023 - 12:05:33'
# Распечатайте полное название месяца из этой даты
# Распечатайте дату в таком формате: "15.01.2023, 12:05"
python_data = datetime.datetime.strptime(data, '%b %d, %Y - %X')
human_date = python_data.strftime('%d.%m.%Y, %I:%M')
human_month = python_data.strftime('%B')
print(python_data)
print(human_month)
print(human_date)
