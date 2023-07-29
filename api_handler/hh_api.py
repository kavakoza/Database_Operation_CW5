import requests


class HH:


    def get_vacancies(self, employer_id: int) -> list:
        params = {
            "per_page": 100,
            "page": 0,
            "area": 113,
        }

        req = requests.get(f"https://api.hh.ru/vacancies?employer_id={employer_id}", params)
        data = req.json()

        hh_list = []
        for item in data["items"]:
            hh_dict = {
                "id": int(item["id"]),
                "title": item["name"],
                "payment": item["salary"]["from"] if item["salary"] else None,
                "description": item["snippet"]["responsobility"],
                "url": item['alternate_url'],
                "employer_id": employer_id,
            }
            if hh_dict["payment"] is not None:
                hh_list.append(hh_dict)

        return hh_list


    def get_company_by_id(self, employer_id: int) -> dict:
        req = requests.get(f"https://api.hh.ru/employers/{employer_id}")
        data = req.json()
        hh_company = {
            "employer_id": int(employer_id),
            "title": data["name"],
            "area": data["area"]["name"],
            "vacancies": data["open_vacancies"],
            "url": data['alternate_url'],
        }
        return hh_company


