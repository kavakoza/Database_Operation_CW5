employers_dict = {
    "Yandex": 1740,
    "VK": 15478,
    "Rambler": 8620,
    "Sber": 3529,
    "Tinkoff": 78638,
    "Megafon": 3127,
    "Ozon": 2180,
    "VTB": 4181,
    "2ГИС": 64174,
    "Lukoil": 907345,
    "Magnit": 49357,
    "Beeline": 4934,
    "MVideo": 2523,
    "MTS": 3776,
    "DNS": 1025275,
}

employers_list = [1740, 15478, 8620, 3529, 78638, 3127, 2180, 4181, 64174, 907345, 49357, 4934, 2523, 3776, 1025275]


def db_dict() -> dict:
    return {"host": "localhost", "database": "hh_vacancies", "user": "postgres", "password": "1234"} #change db_name