import re


def is_valid_email(email):
    # Пример логики валидации email
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None


def is_valid_phone(phone):
    # Пример логики валидации телефона
    phone_pattern = r"^\+7\d{10}$"
    return re.match(phone_pattern, phone) is not None


def is_valid_date(date):
    # Пример логики валидации даты
    date_pattern1 = r"^\d{2}.\d{2}.\d{4}$"
    date_pattern2 = r"^\d{4}-\d{2}-\d{2}$"
    return (
        re.match(date_pattern1, date) is not None
        or re.match(date_pattern2, date) is not None
    )
